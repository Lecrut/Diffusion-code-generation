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
            self.inventory[item_name] = new_quantity
        else:
            raise ValueError(f"Item '{item_name}' not found in inventory.")
    def get_count(self, item_name):
        if item_name in self.inventory:
            return self.inventory[item_name]
        else:
            return 0
def main():
    manager = InventoryManager()
    initial_items = {
        "Apples": 50,
        "Bananas": 120,
        "Oranges": 75
    }
    for item, count in initial_items.items():
        manager.add_item(item, count)
    print("--- Initial Inventory ---")
    print(f"Apples: {manager.get_count('Apples')}")
    print(f"Bananas: {manager.get_count('Bananas')}")
    print(f"Oranges: {manager.get_count('Oranges')}")
    print("\n--- Adding Items ---")
    manager.add_item("Grapes", 200)
    manager.add_item("Apples", 30)
    print(f"Apples after additions: {manager.get_count('Apples')}")
    print(f"Grapes count: {manager.get_count('Grapes')}")
    print("\n--- Updating Item ---")
    manager.update_item("Bananas", 150)
    print(f"Bananas after update: {manager.get_count('Bananas')}")
    print("\n--- Retrieving Non-existent Item ---")
    print(f"Pears count: {manager.get_count('Pears')}")
if __name__ == '__main__':
    main()