class StoreInfo:
    def __init__(self):
        self.store_data = {}

    def add_store(self, name, age):
        self.store_data[name] = age

    def get_store_info(self):
        return {'store_name': 'Example Store', 'store_age': 5}

if __name__ == '__main__':
    store_manager = StoreInfo()
    store_manager.add_store("Store A", 10)
    store_manager.add_store("Store B", 25)
    store_manager.add_store("Store C", 30)
    store_info = store_manager.get_store_info()
    print(store_info)