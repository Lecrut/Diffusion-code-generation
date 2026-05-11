class Inventory:
    def __init__(self):
        self.items = {
            1: {"name": "Laptop", "price": 1200.00},
            2: {"name": "Mouse", "price": 25.50},
            3: {"name": "Keyboard", "price": 75.00},
            4: {"name": "Monitor", "price": 300.00}
        }
    def search_by_id(self, item_id):
        return self.items.get(item_id)
if __name__ == '__main__':
    inventory = Inventory()
    item_id_to_find = 2
    item_details = inventory.search_by_id(item_id_to_find)
    print(f"Searching for item ID: {item_id_to_find}")
    print(item_details)
    item_id_to_find = 99
    item_details = inventory.search_by_id(item_id_to_find)
    print(f"Searching for item ID: {item_id_to_find}")
    print(item_details)