class InventoryManager:
    def __init__(self):
        self.items = []

    def insert(self, item, count):
        if not isinstance(count, int) or count < 0:
            raise ValueError("Count must be a non-negative integer")
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                self.items[i][1] += count
                return
        self.items.append([item, count])

    def update(self, item, count):
        if not isinstance(count, int) or count < 0:
            raise ValueError("Count must be a non-negative integer")
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                self.items[i][1] = max(0, self.items[i][1] + count)
                return
        raise KeyError(f"Item '{item}' not found")

    def delete(self, item):
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                del self.items[i]
                return
        raise KeyError(f"Item '{item}' not found")

    def get_inventory(self):
        return dict(self.items)

if __name__ == '__main__':
    manager = InventoryManager()
    manager.insert("apple", 10)
    manager.update("apple", 5)
    manager.delete("apple")
    print(manager.get_inventory())