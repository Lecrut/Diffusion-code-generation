class ItemManager:
    def __init__(self, items):
        self.items = set(items)

    def get_unique_items(self):
        return list(self.items)

if __name__ == '__main__':
    manager = ItemManager(["banana", "apple", "cherry", "date", "elderberry"])
    unique_items = manager.get_unique_items()
    print(unique_items)