class StoreInventory:
    def __init__(self):
        self.stores = {}
    def add_store(self, store_id):
        if store_id not in self.stores:
            self.stores[store_id] = {}
    def add_product(self, store_id, product_name, stock_level):
        if store_id in self.stores:
            if store_id not in self.stores:
                self.stores[store_id] = {}
            self.stores[store_id][product_name] = stock_level
    def get_stock(self, store_id, product_name):
        if store_id in self.stores and product_name in self.stores[store_id]:
            return self.stores[store_id][product_name]
        return None
    def display_inventory(self):
        for store_id, products in self.stores.items():
            print(f"Store ID: {store_id}")
            for product, stock in products.items():
                print(f"  {product}: {stock}")
if __name__ == '__main__':
    inventory = StoreInventory()
    inventory.add_store("S001")
    inventory.add_store("S002")
    inventory.add_product("S001", "Laptop", 50)
    inventory.add_product("S001", "Mouse", 150)
    inventory.add_product("S001", "Keyboard", 75)
    inventory.add_product("S002", "Laptop", 30)
    inventory.add_product("S002", "Monitor", 100)
    print("--- Inventory Display ---")
    inventory.display_inventory()
    print("\n--- Stock Lookups ---")
    stock1 = inventory.get_stock("S001", "Laptop")
    print(f"Stock of Laptop in S001: {stock1}")
    stock2 = inventory.get_stock("S002", "Monitor")
    print(f"Stock of Monitor in S002: {stock2}")
    stock3 = inventory.get_stock("S999", "Laptop")
    print(f"Stock of Laptop in S999 (Non-existent): {stock3}")