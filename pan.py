import http.client
import json
from prettytable import PrettyTable

conn = http.client.HTTPSConnection("pan-card-verification1.p.rapidapi.com")
mypan=input("Enter your pan card Number")

payload = "{\r\n    \"task_id\": \"74f4c926-250c-43ca-9c53-453e87ceacd1\",\r\n    \"group_id\": \"8e16424a-58fc-4ba4-ab20-5bc8e7c3c41e\",\r\n    \"data\": {\r\n        \"id_number\": \""+mypan+"\"\r\n    }\r\n}"

headers = {
    'content-type': "application/json",
    'X-RapidAPI-Key': "491cb19eaamsh152854c4998f511p1c4251jsn433a9015b971",
    'X-RapidAPI-Host': "pan-card-verification1.p.rapidapi.com"
}

conn.request("POST", "/v3/tasks/sync/verify_with_source/ind_pan", payload, headers)

res = conn.getresponse()
data = res.read()

record=json.loads(data.decode("utf-8"))
dict=record["result"]["source_output"]
myheading=dict.keys()
obj=PrettyTable(myheading) 
data=dict.values()
                
obj.add_row(data)
print(obj)                
                

