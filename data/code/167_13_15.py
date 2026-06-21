import json

def create_store_json():
    store_name = "Tech Innovations"
    age = 10
    data = {
        "store_name": store_name,
        "age": age
    }
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    print(create_store_json())