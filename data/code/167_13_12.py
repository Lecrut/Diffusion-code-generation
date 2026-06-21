import json

class StoreDataCreator:
    STORE_NAME = "Example Store"
    AGE = 5

    @staticmethod
    def create_json():
        data = {
            "store_name": StoreDataCreator.STORE_NAME,
            "age": StoreDataCreator.AGE
        }
        return json.dumps(data, indent=4)

if __name__ == '__main__':
    print(StoreDataCreator.create_json())