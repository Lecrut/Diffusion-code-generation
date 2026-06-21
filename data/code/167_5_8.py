class StoreInfo:
    def __init__(self):
        self.stores = {
            "StoreA": 30,
            "StoreB": 25,
            "StoreC": 35,
            "StoreD": 40,
            "StoreE": 22
        }

    def get_store_age(self, store_name):
        return self.stores.get(store_name, None)

if __name__ == '__main__':
    store_info = StoreInfo()
    print(f"Age of StoreA: {store_info.get_store_age('StoreA')}")
    print(f"Age of StoreB: {store_info.get_store_age('StoreB')}")
    print(f"Age of StoreC: {store_info.get_store_age('StoreC')}")
    print(f"Age of StoreD: {store_info.get_store_age('StoreD')}")
    print(f"Age of StoreE: {store_info.get_store_age('StoreE')}")