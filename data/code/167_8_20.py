class StoreAgeManager:
    STORE_AGE_MAP = {
        "Store X": 25,
        "Store Y": 30,
        "Store Z": 35
    }
    
    @staticmethod
    def get_store_age(store_name):
        return StoreAgeManager.STORE_AGE_MAP.get(store_name, None)

if __name__ == '__main__':
    manager = StoreAgeManager()
    sample_stores = ["Store X", "Store Y", "Store Z", "Store W"]
    for store in sample_stores:
        age = manager.get_store_age(store)
        if age is not None:
            print(f"The age of {store} is {age}")
        else:
            print(f"No data available for {store}")