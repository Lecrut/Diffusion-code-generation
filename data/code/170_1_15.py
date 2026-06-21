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
            print(f'Item added: {item}')

    def get_item(self, item_id):
        return self.items.get(item_id, None)
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item(Item(1, 'Apple', 30))
    inventory.add_item(Item(2, 'Banana', 45))
    print(inventory.get_item(1))
    inventory.add_item(Item(1, 'Apple', 30))