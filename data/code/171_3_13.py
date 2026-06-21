class StoreManager:
    def __init__(self):
        self.stores = {}

    def add_store(self, name, description):
        if name not in self.stores:
            self.stores[name] = description

    def get_store(self, name):
        return self.stores.get(name, None)

    def count_stores(self):
        return len(self.stores)

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store("Store1", "Description of Store 1")
    manager.add_store("Store2", "Description of Store 2")
    print(manager.get_store("Store1"))
    print(manager.count_stores())