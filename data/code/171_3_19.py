class StoreManager:
    DEFAULT_DESCRIPTION = "No description available"

    def __init__(self):
        self.stores = {}

    @staticmethod
    def is_valid_store_name(name):
        return isinstance(name, str) and name.strip()

    def add_store(self, name, description=DEFAULT_DESCRIPTION):
        if not self.is_valid_store_name(name):
            raise ValueError("Invalid store name")
        if name in self.stores:
            raise KeyError(f"Store '{name}' already exists")
        self.stores[name] = description

    def get_store(self, name):
        return self.stores.get(name, StoreManager.DEFAULT_DESCRIPTION)

    def count_stores(self):
        return len(self.stores)

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store("Store A", "Description of Store A")
    manager.add_store("Store B", "Description of Store B")
    print(manager.get_store("Store A"))
    print(manager.count_stores())