class Inventory:

    def __init__(self):
        self.items = []

    def insert(self, item, count):
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                self.items[i][1] += count
                return
        self.items.append([item, count])

    def update(self, item, count):
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                self.items[i][1] = count
                return

    def delete(self, item):
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                del self.items[i]
                return
if __name__ == '__main__':
    inv = Inventory()
    inv.insert('apple', 5)
    inv.insert('banana', 3)
    inv.update('apple', 7)
    inv.delete('banana')
    print(inv.items)