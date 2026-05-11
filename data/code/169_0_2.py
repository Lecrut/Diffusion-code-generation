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
        ("Apples", 100),
        ("Bananas", 150),
        ("Oranges", 75)
    ]
    for item, count in initial_items:
        manager.add_item(item, count)
    print("--- Initial Inventory ---")
    print(f"Apples: {manager.get_count('Apples')}")
    print(f"Bananas: {manager.get_count('Bananas')}")
    print(f"Oranges: {manager.get_count('Oranges')}")
    print("\n--- Updating Inventory ---")
    manager.update_item("Apples", 120)
    print(f"Updated Apples count: {manager.get_count('Apples')}")
    manager.update_item("Bananas", 200)
    print(f"Updated Bananas count: {manager.get_count('Bananas')}")
    print("\n--- Adding New Item ---")
    manager.add_item("Grapes", 300)
    print(f"Grapes count: {manager.get_count('Grapes')}")
    print("\n--- Final Inventory Check ---")
    print(f"Apples: {manager.get_count('Apples')}")
    print(f"Bananas: {manager.get_count('Bananas')}")
    print(f"Oranges: {manager.get_count('Oranges')}")
    print(f"Grapes: {manager.get_count('Grapes')}")
if __name__ == '__main__':
    main()