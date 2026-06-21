class Inventory:

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
            raise ValueError('Not enough stock')

    def query_stock(self, item):
        return self.items.get(item, 0)
if __name__ == '__main__':
    inv = Inventory()
    inv.add_item('apple', 10)
    inv.add_item('banana', 5)
    print(inv.query_stock('apple'))
    inv.remove_item('apple', 3)
    print(inv.query_stock('apple'))