class StoreManager:
    def __init__(self):
        self.stores = {}

    def add_store(self, name, description):
        self.stores[name] = description

    def get_store(self, name):
        return self.stores.get(name)

    def count_stores(self):
        return len(self.stores)

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store("Store1", "This is store 1")
    manager.add_store("Store2", "This is store 2")
    print(manager.get_store("Store1"))
    print(manager.count_stores())