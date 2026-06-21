from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

class Inventory:
    def __init__(self, items):
        self.items = [Item(name, quantity) for name, quantity in items]

    @staticmethod
    def create_inventory(items):
        return Inventory(items)

    def list_items(self):
        for item in self.items:
            print(f"{item.name}: {item.quantity}")

if __name__ == '__main__':
    sample_items = [('apple', 10), ('banana', 5), ('orange', 8)]
    inventory = Inventory.create_inventory(sample_items)
    inventory.list_items()