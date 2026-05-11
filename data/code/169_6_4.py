class ItemManager:
    def __init__(self):
        self.counts = {}
    def update_count(self, item_name, change):
        if item_name in self.counts:
            self.counts[item_name] += change
        else:
            self.counts[item_name] = change
if __name__ == '__main__':
    manager = ItemManager()
    manager.update_count("apple", 10)
    print(f"Apple count after first update: {manager.counts.get('apple')}")
    manager.update_count("banana", 5)
    print(f"Banana count after second update: {manager.counts.get('banana')}")
    manager.update_count("apple", -3)
    print(f"Apple count after third update: {manager.counts.get('apple')}")
    manager.update_count("orange", 20)
    print(f"Orange count after fourth update: {manager.counts.get('orange')}")