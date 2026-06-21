class InventoryManager:

    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            if self.items[item] == 0:
                del self.items[item]
        else:
            raise ValueError('Not enough inventory or item does not exist')

    def get_quantity(self, item):
        return self.items.get(item, 0)
if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item('apples', 30)
    manager.add_item('oranges', 20)
    print(manager.get_quantity('apples'))
    manager.remove_item('apples', 10)
    print(manager.get_quantity('apples'))