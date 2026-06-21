from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

def create_inventory(items):
    return [Item(name, quantity) for name, quantity in items]

def main():
    inventory_items = [('Apples', 30), ('Oranges', 25), ('Bananas', 40)]
    inventory = create_inventory(inventory_items)
    print(inventory)

if __name__ == '__main__':
    main()