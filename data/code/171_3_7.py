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
    manager.add_store("TechZone", "A store for all your tech needs")
    manager.add_store("BookNook", "Your one-stop shop for books and literature")
    print(manager.get_store("TechZone"))
    print(f"Total stores: {manager.count_stores()}")