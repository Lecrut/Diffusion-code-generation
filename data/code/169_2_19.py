from collections import defaultdict

class InventoryManager:
    def __init__(self):
        self.items = defaultdict(int)

    def add_items(self, items: list[tuple[str, int]]):
        for item, count in items:
            self.items[item] += count

    def remove_items(self, item: str, quantity: int) -> bool:
        if self.items[item] >= quantity:
            self.items[item] -= quantity
            return True
        return False

    def check_critical_threshold(self, threshold: int) -> list[str]:
        return [item for item, count in self.items.items() if count < threshold]

if __name__ == '__main__':
    manager = InventoryManager()
    initial_items = [
        ("Apple", 50),
        ("Banana", 100),
        ("Orange", 75),
        ("Grapes", 30)
    ]
    manager.add_items(initial_items)
    
    removed = manager.remove_items("Apple", 20)
    print(f"Removed 20 Apples: {removed}")
    
    critical_items = manager.check_critical_threshold(10)
    print(f"Items below threshold (below 10): {critical_items}")