class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, name, quantity):
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
    def list_inventory(self):
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("Apple", 10)
    inventory.add_item("Banana", 25)
    inventory.add_item("Orange", 15)
    inventory.add_item("Grapes", 30)
    inventory.add_item("Mango", 12)
    print("--- Inventory List ---")
    inventory.list_inventory()