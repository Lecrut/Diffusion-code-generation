from collections import namedtuple
Item = namedtuple('Item', ['id', 'name', 'quantity'])

class Inventory:

    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.id in self.items:
            print(f'Error: Item with id {item.id} already exists.')
        else:
            self.items[item.id] = item
            print(f'Item {item.name} added successfully.')
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item(Item('001', 'Apple', 30))
    inventory.add_item(Item('002', 'Banana', 45))
    inventory.add_item(Item('001', 'Apple', 30))