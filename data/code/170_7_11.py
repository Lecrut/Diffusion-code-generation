class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        return self

    def remove(self, item, quantity):
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            if self.items[item] == 0:
                del self.items[item]
        return self

    def query(self, item):
        return self.items.get(item, 0)

if __name__ == '__main__':
    inv = Inventory()
    print(inv.add('apple', 10).add('banana', 5).remove('apple', 3).query('apple'))