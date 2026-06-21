class Inventory:

    def __init__(self):
        self.items = []

    def insert(self, item):
        index = bisect.bisect_left(self.items, item)
        self.items.insert(index, item)

    def lookup(self, item):
        index = bisect.bisect_left(self.items, item)
        if index != len(self.items) and self.items[index] == item:
            return True
        return False
if __name__ == '__main__':
    inv = Inventory()
    inv.insert('apple')
    inv.insert('banana')
    inv.insert('cherry')
    print(inv.lookup('banana'))
    print(inv.lookup('grape'))