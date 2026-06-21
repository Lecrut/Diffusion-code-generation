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
    manager.add_store("Tech Innovations", "Leading electronics store")
    manager.add_store("Book Haven", "Cozy bookstore with a wide selection")
    print(manager.get_store("Tech Innovations"))
    print(manager.count_stores())