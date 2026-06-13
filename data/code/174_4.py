class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, name, quantity):
        self.items[name] = quantity
    def display_inventory(self):
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")
if __name__ == '__main__':
    my_inventory = Inventory()
    my_inventory.add_item("Laptop", 15)
    my_inventory.add_item("Mouse", 50)
    my_inventory.add_item("Keyboard", 30)
    my_inventory.display_inventory()