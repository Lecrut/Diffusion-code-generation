class SimpleInventory:

    def __init__(self):
        self.items = [0] * 100

    def insert(self, index, count):
        if 0 <= index < len(self.items):
            self.items[index] += count

    def update(self, index, count):
        if 0 <= index < len(self.items):
            self.items[index] = count

    def delete(self, index):
        if 0 <= index < len(self.items):
            self.items[index] = 0
if __name__ == '__main__':
    inventory = SimpleInventory()
    inventory.insert(0, 10)
    inventory.update(1, 5)
    inventory.delete(2)
    print(inventory.items[:3])