from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

def create_inventory(items):
    return [Item(name, quantity) for name, quantity in items]

if __name__ == '__main__':
    inventory_items = [('Apples', 10), ('Oranges', 5), ('Bananas', 7)]
    inventory = create_inventory(inventory_items)
    print([(item.name, item.quantity) for item in inventory])