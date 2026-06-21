import json

class StoreData:
    STORE_NAMES = ["Store A", "Store B", "Store C", "Store D", "Store E"]
    AGE_DATA = [25, 30, 15, 42, 5]

    @staticmethod
    def create_json():
        data = {}
        for store_name, age in zip(StoreData.STORE_NAMES, StoreData.AGE_DATA):
            if isinstance(age, int) and age > 0:
                data[store_name] = age
            else:
                raise ValueError(f"Invalid age {age} for store {store_name}")
        return json.dumps(data, indent=4)

if __name__ == '__main__':
    print(StoreData.create_json())