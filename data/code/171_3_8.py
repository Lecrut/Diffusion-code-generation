class StoreManager:
    STORES = {}

    @staticmethod
    def add_store(name, description):
        if name not in StoreManager.STORES:
            StoreManager.STORES[name] = description

    @staticmethod
    def get_store(name):
        return StoreManager.STORES.get(name, "Store not found")

    @staticmethod
    def count_stores():
        return len(StoreManager.STORES)

if __name__ == '__main__':
    manager = StoreManager()
    manager.add_store("Store A", "Description of Store A")
    manager.add_store("Store B", "Description of Store B")
    print(manager.get_store("Store A"))
    print(manager.count_stores())