from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

def create_inventory(items):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in items):
        raise ValueError("All items must be tuples of (name, quantity)")
    return [Item(name, quantity) for name, quantity in items]

def print_inventory(inventory):
    for item in inventory:
        print(f"{item.name}: {item.quantity}")

if __name__ == '__main__':
    sample_items = [('apple', 10), ('banana', 5), ('orange', 8)]
    try:
        inventory = create_inventory(sample_items)
        print_inventory(inventory)
    except ValueError as e:
        print(e)