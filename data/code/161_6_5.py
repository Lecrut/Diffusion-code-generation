from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

class Inventory:
    def __init__(self, items):
        self.items = [Item(name, quantity) for name, quantity in items]

    def add_item(self, name, quantity):
        self.items.append(Item(name, quantity))

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def list_items(self):
        return [f"{item.name}: {item.quantity}" for item in self.items]

if __name__ == '__main__':
    sample_items = [('apple', 10), ('banana', 5), ('orange', 8)]
    inventory = Inventory(sample_items)
    
    print("Initial Inventory:")
    print(*inventory.list_items(), sep='\n')
    
    inventory.add_item('grape', 20)
    print("\nInventory after adding grapes:")
    print(*inventory.list_items(), sep='\n')
    
    inventory.remove_item('banana')
    print("\nInventory after removing bananas:")
    print(*inventory.list_items(), sep='\n')