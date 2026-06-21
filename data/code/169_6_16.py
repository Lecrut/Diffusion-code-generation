from collections import defaultdict

class ItemManager:
    def __init__(self):
        self.counts = defaultdict(int)

    def get_counts(self) -> dict:
        return {item: count for item, count in self.counts.items() if count > 0}

    def reset(self):
        self.counts.clear()

    def clone(self) -> 'ItemManager':
        new_manager = ItemManager()
        new_manager.counts.update(self.counts)
        return new_manager

if __name__ == '__main__':
    manager = ItemManager()
    manager.counts[101] += 5
    print(f"Count for 101 after first update: {manager.get_counts().get(101, 0)}")
    manager.counts[101] -= 2
    print(f"Count for 101 after second update: {manager.get_counts().get(101, 0)}")
    manager.counts[202] += 10
    print(f"Count for 202: {manager.get_counts().get(202, 0)}")
    manager.counts[101] += 100
    print(f"Count for 101 after third update: {manager.get_counts().get(101, 0)}")

    cloned_manager = manager.clone()
    cloned_manager.counts[103] += 5
    print(f"Cloned count for 101: {cloned_manager.get_counts().get(101, 0)}")
    print(f"Cloned count for 103: {cloned_manager.get_counts().get(103, 0)}")

    manager.reset()
    print(f"After reset, count for 101: {manager.get_counts().get(101, 0)}")