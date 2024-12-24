import requests
import json
import threading

url='https://dummyjson.com/products'
r=requests.get(url)

if r.status_code==200:
    data=r.json()
    with open('products.json', 'w',) as f:
        json.dump(data,f,indent=4)
        print('Data saved')
else:
    print('something went wrong')

    #  2 masala
def download_products(url):
    r=requests.get(url)
    data=r.json()
    with open('data.json', 'w') as f:
        json.dump(data,f,indent=4)
        print('Data saved sucessfully')
def download_products_thread(url):
    r=requests.get(url)
    data=r.json()
    with open('data.json', 'w') as f:
        json.dump(data,f,indent=4)
        print('Data saved successfully')

url=[
    'https://dummyjson.com/products',
    'https://jsonplaceholder.typicode.com/posts'
]

t1=threading.Thread(target=download_products, args=(url[0],))
t2=threading.Thread(target=download_products_thread, args=(url[1],))

t1.start()
t2.start()

t1.join()
t2.join()
