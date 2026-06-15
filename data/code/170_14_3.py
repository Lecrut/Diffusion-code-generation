class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
    def display_inventory(self):
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")
if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 120)
    my_inventory.add_item("Oranges", 75)
    my_inventory.add_item("Grapes", 30)
    print("--- Inventory State ---")
    my_inventory.display_inventory()