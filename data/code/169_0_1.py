class InventoryManager:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
    def update_item(self, item_name, new_quantity):
        if item_name in self.inventory:
            if new_quantity >= 0:
                self.inventory[item_name] = new_quantity
            else:
                raise ValueError("Quantity cannot be negative.")
        else:
            raise KeyError(f"Item '{item_name}' not found in inventory.")
    def get_count(self, item_name):
        if item_name in self.inventory:
            return self.inventory[item_name]
        else:
            return 0
def manage_inventory():
    manager = InventoryManager()
    initial_items = {
        "Apples": 50,
        "Bananas": 120,
        "Oranges": 75
    }
    for item, count in initial_items.items():
        manager.add_item(item, count)
    print("--- Initial Inventory State ---")
    print(manager.inventory)
    print("\n--- Operations ---")
    manager.add_item("Grapes", 300)
    print(f"Added 300 Grapes. Current inventory: {manager.inventory}")
    manager.update_item("Apples", 65)
    print(f"Updated Apples count. Current inventory: {manager.inventory}")
    try:
        manager.update_item("Pears", 100)
    except KeyError as e:
        print(f"Error: {e}")
    try:
        manager.get_count("Pears")
    except KeyError:
        print("Pears count: 0")
    try:
        manager.get_count("Watermelons")
    except KeyError:
        print("Watermelons count: 0")
    print("\n--- Final Inventory State ---")
    print(manager.inventory)
if __name__ == '__main__':
    manage_inventory()