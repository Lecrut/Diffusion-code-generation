import json

def create_store_json():
    store_data = {
        "store_name": "Central Market",
        "age": 10
    }
    return json.dumps(store_data, indent=4)

if __name__ == '__main__':
    print(create_store_json())