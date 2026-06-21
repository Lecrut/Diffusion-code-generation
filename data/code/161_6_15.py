from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

def create_inventory():
    return [Item('apple', 3), Item('banana', 5), Item('cherry', 2)]

if __name__ == '__main__':
    inventory = create_inventory()
    print(inventory)