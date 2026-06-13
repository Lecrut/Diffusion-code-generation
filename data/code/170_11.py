class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
    def view_inventory(self):
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")
if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Apples", 50)
    my_inventory.add_item("Bananas", 120)
    my_inventory.add_item("Oranges", 75)
    my_inventory.view_inventory()