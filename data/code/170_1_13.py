from collections import namedtuple
Item = namedtuple('Item', 'id name quantity')

class Inventory:

    def __init__(self):
        self.items = {}

    def add_item(self, item_id, details):
        if item_id in self.items:
            print(f'Error: Item {item_id} already exists.')
        else:
            self.items[item_id] = details
            print(f'Item {item_id} added successfully.')

    def get_item(self, item_id):
        return self.items.get(item_id)
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('A001', {'name': 'Laptop', 'quantity': 10, 'price': 1200.0})
    inventory.add_item('B002', {'name': 'Mouse', 'quantity': 50, 'price': 25.5})
    inventory.add_item('C003', {'name': 'Keyboard', 'quantity': 30, 'price': 75.0})
    print(inventory.get_item('A001'))
    print(inventory.get_item('B002'))
    print(inventory.get_item('C003'))
    inventory.add_item('A001', {'name': 'Laptop', 'quantity': 10, 'price': 1200.0})