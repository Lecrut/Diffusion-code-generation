class ItemManager:
    def __init__(self):
        self.counts = {}
    def update_count(self, item_id, change):
        if item_id in self.counts:
            self.counts[item_id] += change
        else:
            self.counts[item_id] = change
if __name__ == '__main__':
    manager = ItemManager()
    manager.update_count(101, 5)
    print(f"Count for 101: {manager.counts.get(101)}")
    manager.update_count(102, 10)
    print(f"Count for 102: {manager.counts.get(102)}")
    manager.update_count(101, -2)
    print(f"Count for 101: {manager.counts.get(101)}")
    manager.update_count(103, 1)
    print(f"Count for 103: {manager.counts.get(103)}")