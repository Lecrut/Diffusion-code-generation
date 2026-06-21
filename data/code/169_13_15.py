class ItemInventory:
    def __init__(self):
        self.items = [0] * 100

    def insert(self, item_id, count):
        if 0 <= item_id < len(self.items):
            self.items[item_id] += count

    def update(self, item_id, count):
        if 0 <= item_id < len(self.items):
            self.items[item_id] = count

    def delete(self, item_id):
        if 0 <= item_id < len(self.items):
            self.items[item_id] = 0

if __name__ == '__main__':
    inventory = ItemInventory()
    inventory.insert(10, 5)
    inventory.update(20, 3)
    inventory.delete(10)
    print(inventory.items[10])
    print(inventory.items[20])