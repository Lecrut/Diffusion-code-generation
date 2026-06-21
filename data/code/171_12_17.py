class StoreManager:
    _STORES = [
        {"store_name": "Store A", "description": "A large retail location"},
        {"store_name": "Store B", "description": "Small boutique shop"},
        {"store_name": "Store C", "description": "Warehouse and distribution center"}
    ]

    @staticmethod
    def initialize_stores():
        return StoreManager._STORES.copy()

    @staticmethod
    def update_store_description(stores, store_name, new_description):
        for store in stores:
            if store["store_name"] == store_name:
                store["description"] = new_description
                break

    @staticmethod
    def get_stores_sorted_by_name(stores):
        return sorted(stores, key=lambda x: x["store_name"])

if __name__ == '__main__':
    stores = StoreManager.initialize_stores()
    StoreManager.update_store_description(stores, "Store B", "Updated boutique shop")
    sorted_stores = StoreManager.get_stores_sorted_by_name(stores)
    print(sorted_stores)