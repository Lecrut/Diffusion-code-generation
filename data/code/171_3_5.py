class StoreManager:
    def __init__(self):
        self.stores = {}

    def add_store(self, name, description):
        if not isinstance(name, str) or not isinstance(description, str):
            raise ValueError("Name and description must be strings")
        if name in self.stores:
            raise ValueError(f"Store '{name}' already exists")
        self.stores[name] = description

    def get_store(self, name):
        return self.stores.get(name, "Store not found")

    def count_stores(self):
        return len(self.stores)

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store("Store A", "Description of Store A")
    manager.add_store("Store B", "Description of Store B")
    print(manager.get_store("Store A"))
    print(manager.count_stores())