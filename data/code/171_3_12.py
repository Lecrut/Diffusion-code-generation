class StoreManager:
    def __init__(self):
        self.stores = {}
    
    def add_store(self, name, description):
        if not isinstance(name, str) or not isinstance(description, str):
            raise ValueError("Name and description must be strings")
        if name in self.stores:
            raise KeyError(f"Store '{name}' already exists")
        self.stores[name] = description
    
    def get_store(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        return self.stores.get(name, None)
    
    def count_stores(self):
        return len(self.stores)

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store("Store A", "Description of Store A")
    manager.add_store("Store B", "Description of Store B")
    print(manager.get_store("Store A"))
    print(manager.count_stores())