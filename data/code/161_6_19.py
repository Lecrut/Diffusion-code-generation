from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity):
        self.items.append(Item(name, quantity))

    def list_items(self):
        for item in self.items:
            print(f"{item.name}: {item.quantity}")

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('apple', 10)
    inventory.add_item('banana', 5)
    inventory.list_items()