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
if __name__ == '__main__':
    inventory = Inventory()
    item1_details = {'name': 'Laptop', 'quantity': 10, 'price': 1200.0}
    inventory.add_item('A001', item1_details)
    item2_details = {'name': 'Mouse', 'quantity': 50, 'price': 25.5}
    inventory.add_item('B002', item2_details)
    item3_details = {'name': 'Keyboard', 'quantity': 30, 'price': 75.0}
    try:
        inventory.add_item('A001', item1_details)
    except Exception as e:
        print(e)
    print('Inventory contents:')
    for item_id, details in inventory.items.items():
        print(f'ID: {item_id}, Details: {details}')