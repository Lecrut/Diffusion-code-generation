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
            raise ValueError('Not enough stock to remove')

    def query_stock(self, item):
        return self.items.get(item, 0)
if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.add_item('apples', 30)
    inventory.add_item('oranges', 20)
    print(inventory.query_stock('apples'))
    inventory.remove_item('apples', 10)
    print(inventory.query_stock('apples'))