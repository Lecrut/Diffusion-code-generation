from collections import namedtuple

Item = namedtuple('Item', 'item_id name quantity price')

class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item):
        if item.item_id in self.items:
            print(f'Error: Item {item.item_id} already exists.')
        else:
            self.items[item.item_id] = item
            print(f'Item {item.item_id} added successfully.')

if __name__ == '__main__':
    inventory = Inventory()
    item1 = Item('A001', 'Laptop', 10, 1200.00)
    item2 = Item('B002', 'Mouse', 50, 25.50)
    item3 = Item('C003', 'Keyboard', 30, 75.00)

    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)