class InventoryManager:
    def __init__(self):
        self.inventory = {}
    def initialize_inventory(self, initial_items):
        for item, count in initial_items.items():
            self.inventory[item] = count
    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
    def update_count(self, item, new_count):
        if item in self.inventory:
            self.inventory[item] = new_count
    def display_inventory(self):
        print("--- Current Inventory ---")
        if not self.inventory:
            print("Inventory is empty.")
            return
        for item, count in sorted(self.inventory.items()):
            print(f"{item}: {count}")
        print("------------------------")
if __name__ == '__main__':
    manager = InventoryManager()
    initial_data = {
        "Apples": 50,
        "Bananas": 120
    }
    manager.initialize_inventory(initial_data)
    manager.display_inventory()
    manager.add_item("Apples", 30)
    manager.add_item("Oranges", 75)
    manager.update_count("Bananas", 150)
    manager.display_inventory()