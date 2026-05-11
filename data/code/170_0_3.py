class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                print(f"Error: Insufficient quantity of {item_name} to remove.")
        else:
            print(f"Error: {item_name} not found in inventory.")
    def list_items(self):
        if not self.items:
            print("Inventory is empty.")
            return
        print("Current Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")
if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 100)
    my_inventory.add_item("Oranges", 75)
    my_inventory.list_items()
    my_inventory.add_item("Apples", 20)
    my_inventory.list_items()
    my_inventory.remove_item("Bananas", 30)
    my_inventory.remove_item("Grapes", 10)
    my_inventory.list_items()
    my_inventory.remove_item("Apples", 100)
    my_inventory.list_items()
    my_inventory.remove_item("Oranges", 100)
    my_inventory.list_items()