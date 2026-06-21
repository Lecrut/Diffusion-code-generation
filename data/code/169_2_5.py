from typing import Dict

class InventoryManager:
    def __init__(self):
        self.items: Dict[str, int] = {}

    def add_items(self, items: Dict[str, int]) -> None:
        for item, quantity in items.items():
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity

    def remove_items(self, item: str, quantity: int) -> bool:
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            return True
        return False

    def check_critical_threshold(self, threshold: int) -> Dict[str, bool]:
        return {item: count < threshold for item, count in self.items.items()}

if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_items({'apples': 10, 'bananas': 5})
    print(manager.remove_items('apples', 3))
    print(manager.check_critical_threshold(2))