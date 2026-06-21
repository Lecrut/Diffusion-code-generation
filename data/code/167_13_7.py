import json

class StoreData:
    def __init__(self):
        self.data = {
            "store_name": "Example Store",
            "age": 5
        }

    def get_json(self):
        return json.dumps(self.data, indent=4)

if __name__ == '__main__':
    store_instance = StoreData()
    print(store_instance.get_json())