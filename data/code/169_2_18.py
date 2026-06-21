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
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            return True
        return False

    def check_critical_threshold(self, threshold: int) -> Dict[str, int]:
        return {item: count for item, count in self.items.items() if count < threshold}

if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.add_items({'apple': 10, 'banana': 5})
    print(inventory.remove_items('apple', 3))
    print(inventory.check_critical_threshold(2))