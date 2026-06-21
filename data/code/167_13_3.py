import json

def create_store_json():
    data = {
        "store_name": "Example Store",
        "age": 5
    }
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    print(create_store_json())