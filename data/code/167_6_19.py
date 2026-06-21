class StoreData:
    def __init__(self, store_names, ages):
        self.store_dict = dict(zip(store_names, ages))

    def get_store_age(self, store_name):
        return self.store_dict.get(store_name)

if __name__ == '__main__':
    store_names = ["Store A", "Store B", "Store C"]
    ages = [5, 3, 8]
    
    store_data = StoreData(store_names, ages)
    
    print(f"Age of Store A: {store_data.get_store_age('Store A')}")
    print(f"Age of Store B: {store_data.get_store_age('Store B')}")
    print(f"Age of Store C: {store_data.get_store_age('Store C')}")