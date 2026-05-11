class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
    def list_inventory(self):
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("Apples", 10)
    inventory.add_item("Bananas", 15)
    inventory.add_item("Oranges", 20)
    inventory.add_item("Grapes", 5)
    inventory.add_item("Pears", 12)
    print("--- Inventory List ---")
    inventory.list_inventory()