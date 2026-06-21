class StoreAgeManager:
    STORE_AGE_MAP = {
        "Store Alpha": 25,
        "Store Beta": 30,
        "Store Gamma": 35
    }

    def get_store_age(self, store_name):
        return self.STORE_AGE_MAP.get(store_name, None)

if __name__ == '__main__':
    manager = StoreAgeManager()
    sample_stores = ["Store Alpha", "Store Beta", "Store Delta"]
    for store in sample_stores:
        print(f"The age of {store} is {manager.get_store_age(store)}")