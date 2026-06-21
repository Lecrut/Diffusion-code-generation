from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity):
        item = Item(name, quantity)
        self.items.append(item)

    def get_inventory(self):
        return self.items

def main():
    inventory = Inventory()
    inventory.add_item('Apples', 30)
    inventory.add_item('Oranges', 25)
    inventory.add_item('Bananas', 40)

    for item in inventory.get_inventory():
        print(f"{item.name}: {item.quantity}")

if __name__ == '__main__':
    main()