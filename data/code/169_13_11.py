class InventoryManager:

    def __init__(self):
        self.items = []

    def insert_item(self, item_name, count):
        if not isinstance(item_name, str) or not isinstance(count, (int, float)) or count < 0:
            raise ValueError('Invalid input for item name and count')
        for i in range(len(self.items)):
            if self.items[i][0] == item_name:
                self.items[i] = (item_name, self.items[i][1] + count)
                return
        self.items.append((item_name, int(count)))

    def update_item_count(self, item_name, count):
        if not isinstance(item_name, str) or not isinstance(count, (int, float)) or count < 0:
            raise ValueError('Invalid input for item name and count')
        for i in range(len(self.items)):
            if self.items[i][0] == item_name:
                self.items[i] = (item_name, int(self.items[i][1]) + int(count))
                return
        raise KeyError(f'Item {item_name} not found')

    def delete_item(self, item_name):
        if not isinstance(item_name, str):
            raise ValueError('Invalid input for item name')
        for i in range(len(self.items)):
            if self.items[i][0] == item_name:
                del self.items[i]
                return
        raise KeyError(f'Item {item_name} not found')
if __name__ == '__main__':
    manager = InventoryManager()
    manager.insert_item('apple', 10)
    print(manager.items)
    manager.update_item_count('apple', 5)
    print(manager.items)
    manager.delete_item('apple')
    print(manager.items)