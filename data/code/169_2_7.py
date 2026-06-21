from typing import Dict, List, Optional

class InventoryManager:
    def __init__(self):
        self.items: Dict[str, int] = {}

    def add_items(self, items: Dict[str, int]) -> None:
        for item, count in items.items():
            if not isinstance(item, str) or not isinstance(count, int) or count < 0:
                raise ValueError("Invalid input. Item must be a string and count must be a non-negative integer.")
            if item in self.items:
                self.items[item] += count
            else:
                self.items[item] = count

    def remove_items(self, item: str, quantity: int) -> None:
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid input. Item must be a string and quantity must be a non-negative integer.")
        if item in self.items:
            if self.items[item] >= quantity:
                self.items[item] -= quantity
                if self.items[item] == 0:
                    del self.items[item]
            else:
                raise ValueError(f"Not enough {item} to remove.")

    def check_critical_threshold(self, threshold: int) -> List[str]:
        return [item for item, count in self.items.items() if count < threshold]

if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.add_items({"Apple": 10, "Banana": 5})
    inventory.remove_items("Apple", 3)
    print(inventory.check_critical_threshold(2))