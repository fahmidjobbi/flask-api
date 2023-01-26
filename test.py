import requests
base=r'http://localhost:5000'
#response=requests.put(base+'/video/1',json={"likes":10,"name":"Tim","views":100})
data=[
   {"likes":10,"name":"joe","views":1000},
   {"likes":5,"name":"Tim","views":10000},
   {"likes":2,"name":"Fahmi","views":105},
   {"likes":14,"name":"loiiuuy","views":177},
]
for i in range(len(data)):
    response=requests.put(base+'/video/'+str(i),json=data[i])
    print(response.json())

#response=requests.delete(base+'/video/0')
#print(response)

response=requests.patch(base+'/video/2',json={"views":99}  )
print(response.json())

#response=requests.get(base+'/video/2')
#print(response.json())

#response=requests.get(base+'/video/6')
#print(response.json())

