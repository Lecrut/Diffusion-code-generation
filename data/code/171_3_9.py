class Store:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class StoreManager:
    def __init__(self):
        self.stores = {}

    def add_store(self, store):
        if isinstance(store, Store) and store.name not in self.stores:
            self.stores[store.name] = store

    def get_store(self, name):
        return self.stores.get(name, None)

    def count_stores(self):
        return len(self.stores)

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store(Store("Store A", "Description of Store A"))
    manager.add_store(Store("Store B", "Description of Store B"))
    print(manager.get_store("Store A").description)
    print(manager.count_stores())