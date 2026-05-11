class StoreData:
    def __init__(self):
        self.stores = {}
    def add_store(self, name, age):
        self.stores[name] = age
    def get_all_data(self):
        return self.stores
if __name__ == '__main__':
    data_manager = StoreData()
    data_manager.add_store("Store A", 10)
    data_manager.add_store("Store B", 25)
    data_manager.add_store("Store C", 30)
    all_data = data_manager.get_all_data()
    print(all_data)