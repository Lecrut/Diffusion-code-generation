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
def main():
    manager = InventoryManager()
    initial_items = [
        ("Apples", 50),
        ("Bananas", 120),
        ("Oranges", 75)
    ]
    for item, count in initial_items:
        manager.add_item(item, count)
    print("--- Initial Inventory ---")
    print(f"Apples count: {manager.get_count('Apples')}")
    print(f"Bananas count: {manager.get_count('Bananas')}")
    print(f"Oranges count: {manager.get_count('Oranges')}")
    print("\n--- Updating Inventory ---")
    manager.update_item("Apples", 65)
    print(f"Apples count after update: {manager.get_count('Apples')}")
    manager.update_item("Bananas", 150)
    print(f"Bananas count after update: {manager.get_count('Bananas')}")
    print("\n--- Adding New Item ---")
    manager.add_item("Grapes", 200)
    print(f"Grapes count: {manager.get_count('Grapes')}")
    print("\n--- Final Inventory Check ---")
    for item in manager.inventory.keys():
        print(f"{item}: {manager.inventory[item]}")
if __name__ == '__main__':
    main()