class InventorySystem:

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid item or quantity')
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity):
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid item or quantity')
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            if self.items[item] == 0:
                del self.items[item]
        else:
            raise KeyError('Item not found or insufficient quantity')

    def get_item(self, item):
        if not isinstance(item, str):
            raise ValueError('Invalid item')
        return self.items.get(item, 0)

    def update_quantity(self, item, quantity):
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid item or quantity')
        if item in self.items:
            self.items[item] = quantity
        else:
            raise KeyError('Item not found')
if __name__ == '__main__':
    inventory = InventorySystem()
    inventory.add_item('apple', 10)
    print(inventory.get_item('apple'))
    inventory.remove_item('apple', 5)
    print(inventory.get_item('apple'))
    inventory.update_quantity('apple', 20)
    print(inventory.get_item('apple'))