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
    inventory = Inventory()
    inventory.add_item("Apples", 50)
    inventory.add_item("Bananas", 120)
    inventory.add_item("Oranges", 75)
    inventory.view_inventory()