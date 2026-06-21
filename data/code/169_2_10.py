from typing import Dict

class InventoryManager:
    def __init__(self):
        self.items: Dict[str, int] = {}

    def add_items(self, items: Dict[str, int]) -> None:
        for item, count in items.items():
            if item in self.items:
                self.items[item] += count
            else:
                self.items[item] = count

    def remove_items(self, item: str, quantity: int) -> bool:
        if item not in self.items or self.items[item] < quantity:
            return False
        self.items[item] -= quantity
        if self.items[item] == 0:
            del self.items[item]
        return True

    def check_critical_threshold(self, threshold: int) -> bool:
        for count in self.items.values():
            if count < threshold:
                return True
        return False

if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_items({'apples': 10, 'bananas': 5})
    manager.remove_items('apples', 3)
    print(manager.check_critical_threshold(2))