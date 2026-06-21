class StoreAgeManager:
    STORE_AGE_MAP = {
        "Store Alpha": 25,
        "Store Beta": 30,
        "Store Gamma": 35
    }

    @staticmethod
    def get_store_age(store_name):
        return StoreAgeManager.STORE_AGE_MAP.get(store_name, None)

if __name__ == '__main__':
    manager = StoreAgeManager()
    sample_stores = ["Store Alpha", "Store Beta", "Store Gamma"]
    for store in sample_stores:
        print(f"The age of {store} is {manager.get_store_age(store)}")