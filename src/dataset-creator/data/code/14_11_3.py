class InventoryManager:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
    def get_quantity(self, item_name):
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
    manager.add_item("Apples", 30)
    print("Item count for Apples:", manager.get_quantity("Apples"))
    print("Item count for Bananas:", manager.get_quantity("Bananas"))
    print("Item count for Grapes:", manager.get_quantity("Grapes"))
    manager.display_inventory()