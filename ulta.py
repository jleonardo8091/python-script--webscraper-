from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import webbrowser

url='http://www.ulta.com/promotion/sale'

page=ureq(url)
htmlpage=page.read()
page.close()
pagesoup=soup(htmlpage,'html.parser')

item_list=[]
sale_list=[]
containers=pagesoup.findAll('p',{'class':'prod-desc'})
containers2=pagesoup.findAll('div',{'class':'productSale'})
for container in containers:
    item=container.a.next
    item_list.append(item)
    
for container in containers2:
    sale=container.span.next
    sale_list.append(sale)

filename="products.csv"
f=open(filename,'w')
itemlist=[s.strip('\r\n\t\t\t') for s in item_list]


salelist=[s.strip(' \r\n\t\t\t\t\t\t') for s in sale_list]


c=[]

headers="Product_Name_and_Price\n"
f.write(headers)

'''This section iterates among 2 list and appends
each item to a new list using zip()'''
for x,y in zip(itemlist,salelist):
    c.append(x)
    c.append(y)
'''This section creates a variable "it" to iterate
list c. then uses a for loop to print the first
item "i" and the item right next to it'''
print("You can find the following deals by going to\n ",url,"\n")
it =iter(c)    
for  i in it:
    print(i,next(it))


for i in c:
    f.write(i+"\n")

f.close()

input('\nIf you find anything yo are looking for,\n press enter to go this deals page...')
webbrowser.open(url)
