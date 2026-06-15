class InventoryManager:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
    def get_item_count(self, item_name):
        return self.inventory.get(item_name, 0)
    def display_inventory(self):
        print("--- Inventory ---")
        if not self.inventory:
            print("Inventory is empty.")
            return
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")
        print("-----------------")
if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item("Apples", 50)
    manager.add_item("Bananas", 120)
    manager.add_item("Oranges", 75)
    manager.add_item("Grapes", 30)
    manager.add_item("Apples", 25)
    print(f"Quantity of Apples: {manager.get_item_count('Apples')}")
    print(f"Quantity of Bananas: {manager.get_item_count('Bananas')}")
    print(f"Quantity of Pears: {manager.get_item_count('Pears')}")
    manager.display_inventory()