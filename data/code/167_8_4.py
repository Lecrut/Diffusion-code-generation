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
    sample_store = "Store Beta"
    print(f"The age of {sample_store} is {StoreAgeManager.get_store_age(sample_store)}")