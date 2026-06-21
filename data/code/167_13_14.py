import json

def create_json():
    data = {
        "store_name": "Example Store",
        "age": 50
    }
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    print(create_json())