class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
    def remove_item(self, item_name, quantity):
        if item_name not in self.items:
            return False
        if self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
            return True
        else:
            return False
    def display_inventory(self):
        if not self.items:
            print("Inventory is empty.")
            return
        print("--- Current Inventory ---")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")
        print("-------------------------")
if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 120)
    my_inventory.add_item("Oranges", 75)
    my_inventory.display_inventory()
    print("\nAttempting to remove items:")
    success = my_inventory.remove_item("Apples", 10)
    print(f"Removed 10 Apples: {success}")
    success = my_inventory.remove_item("Bananas", 50)
    print(f"Removed 50 Bananas: {success}")
    success = my_inventory.remove_item("Grapes", 20)
    print(f"Removed 20 Grapes (non-existent): {success}")
    my_inventory.display_inventory()
    success = my_inventory.remove_item("Oranges", 100)
    print(f"Removed 100 Oranges: {success}")
    my_inventory.display_inventory()