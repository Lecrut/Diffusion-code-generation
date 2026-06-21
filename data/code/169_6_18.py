from collections import defaultdict

class ItemManager:
    def __init__(self):
        self.counts = defaultdict(int)

    def update_count(self, item_id, change):
        if not isinstance(item_id, int) or not isinstance(change, (int, float)):
            raise ValueError("Invalid input type")
        self.counts[item_id] += change

    def get_counts(self):
        return {item_id: count for item_id, count in self.counts.items() if count > 0}

    def reset_count(self, item_id=None):
        if item_id is None:
            self.counts.clear()
        elif isinstance(item_id, int) and item_id in self.counts:
            del self.counts[item_id]

    def clone(self):
        new_manager = ItemManager()
        new_manager.counts.update(self.counts)
        return new_manager

if __name__ == '__main__':
    manager = ItemManager()
    manager.update_count(101, 5)
    print(f"Count for 101: {manager.get_counts()}")
    manager.update_count(101, -2)
    print(f"Count for 101 after update: {manager.get_counts()}")
    manager.update_count(202, 10)
    print(f"Count for 202: {manager.get_counts()}")
    manager.update_count(101, 100)
    print(f"Count for 101 after third update: {manager.get_counts()}")
    manager.reset_count(101)
    print(f"Count for 101 after reset: {manager.get_counts()}")
    cloned_manager = manager.clone()
    cloned_manager.update_count(203, 5)
    print(f"Cloned count for 203: {cloned_manager.get_counts()}")