from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

def create_inventory():
    inventory = [
        Item('Apples', 30),
        Item('Oranges', 45),
        Item('Bananas', 20)
    ]
    return inventory

if __name__ == '__main__':
    inventory = create_inventory()
    for item in inventory:
        print(f"{item.name}: {item.quantity}")