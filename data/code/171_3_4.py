class StoreManager:
    def __init__(self):
        self.stores = {}

    def add_store(self, name, description):
        if not name or not isinstance(name, str):
            raise ValueError("Store name must be a non-empty string")
        if not description or not isinstance(description, str):
            raise ValueError("Store description must be a non-empty string")
        if name in self.stores:
            raise ValueError(f"Store with name '{name}' already exists")
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