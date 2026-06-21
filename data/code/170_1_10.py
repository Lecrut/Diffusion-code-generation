from collections import namedtuple
Item = namedtuple('Item', ['id', 'name', 'quantity'])

class Inventory:

    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.id in self.items:
            raise ValueError(f'Duplicate item ID: {item.id}')
        self.items[item.id] = item

    def get_item(self, item_id):
        return self.items.get(item_id)
if __name__ == '__main__':
    inventory = Inventory()
    try:
        inventory.add_item(Item(id=1, name='apple', quantity=30))
        print(inventory.get_item(1))
        inventory.add_item(Item(id=2, name='banana', quantity=45))
        print(inventory.get_item(2))
        inventory.add_item(Item(id=1, name='apple', quantity=30))
    except ValueError as e:
        print(e)