class InventoryManager:

    def __init__(self):
        self.items = []

    def insert_item(self, item, count):
        if not isinstance(count, int) or count < 0:
            raise ValueError('Count must be a non-negative integer')
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                self.items[i][1] += count
                return
        self.items.append([item, count])

    def update_item(self, item, count):
        if not isinstance(count, int) or count < 0:
            raise ValueError('Count must be a non-negative integer')
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                self.items[i][1] = count
                return
        raise KeyError(f"Item '{item}' not found")

    def delete_item(self, item):
        for i in range(len(self.items)):
            if self.items[i][0] == item:
                del self.items[i]
                return
        raise KeyError(f"Item '{item}' not found")
if __name__ == '__main__':
    manager = InventoryManager()
    manager.insert_item('apple', 10)
    manager.insert_item('banana', 5)
    print(manager.items)
    manager.update_item('apple', 20)
    print(manager.items)
    manager.delete_item('banana')
    print(manager.items)