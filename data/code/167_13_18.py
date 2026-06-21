import json
JSON_INDENT = 4

def create_store_json():
    store_name = 'Example Store'
    age = 5
    data = {'store_name': store_name, 'age': age}
    json_string = json.dumps(data, indent=JSON_INDENT)
    return json_string
if __name__ == '__main__':
    print(create_store_json())