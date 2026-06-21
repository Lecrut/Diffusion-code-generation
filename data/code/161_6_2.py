from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

def create_inventory(items):
    return [Item(name, quantity) for name, quantity in items]

if __name__ == '__main__':
    sample_items = [('apple', 10), ('banana', 5), ('orange', 8)]
    inventory = create_inventory(sample_items)
    print(inventory)