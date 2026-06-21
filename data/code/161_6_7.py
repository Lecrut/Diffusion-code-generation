from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

def create_inventory(items):
    return [Item(name, quantity) for name, quantity in items]

def print_inventory(inventory):
    for item in inventory:
        print(f"{item.name}: {item.quantity}")

if __name__ == '__main__':
    sample_items = [('Apples', 10), ('Oranges', 5), ('Bananas', 20)]
    inventory = create_inventory(sample_items)
    print_inventory(inventory)