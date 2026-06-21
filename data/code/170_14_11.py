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
            raise ValueError("Not enough inventory or item does not exist")

    def list_items(self):
        return self.items

if __name__ == '__main__':
    inv = Inventory()
    inv.add_item('apples', 10)
    inv.add_item('oranges', 5)
    print(inv.list_items())
    inv.remove_item('apples', 3)
    print(inv.list_items())