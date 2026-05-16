class StoreData:
    def __init__(self):
        self.stores = {}
    def add_store(self, name, age):
        self.stores[name] = age
    def get_all_data(self):
        return self.stores
if __name__ == '__main__':
    data_store = StoreData()
    data_store.add_store("StoreA", 10)
    data_store.add_store("StoreB", 25)
    data_store.add_store("StoreC", 30)
    all_data = data_store.get_all_data()
    print(all_data)