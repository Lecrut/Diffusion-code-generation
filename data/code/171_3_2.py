class StoreManager:
    def __init__(self):
        self.stores = {}

    def add_store(self, name, description):
        self.stores[name] = description

    def get_store(self, name):
        return self.stores.get(name, None)

    def count_stores(self):
        return len(self.stores)

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store("Store A", "Description of Store A")
    manager.add_store("Store B", "Description of Store B")
    print(manager.get_store("Store A"))
    print(manager.count_stores())