class InventoryManager:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
        else:
            raise ValueError('Not enough stock or item does not exist')

    def query_stock(self, item_name):
        return self.items.get(item_name, 0)
if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.add_item('apples', 30)
    inventory.add_item('oranges', 20)
    print(inventory.query_stock('apples'))
    inventory.remove_item('apples', 10)
    print(inventory.query_stock('apples'))