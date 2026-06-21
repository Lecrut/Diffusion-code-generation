from typing import Dict

class InventoryManager:
    def __init__(self, critical_threshold: int = 10):
        self.inventory: Dict[str, int] = {}
        self.critical_threshold = critical_threshold

    def add_items(self, items: Dict[str, int]) -> None:
        for item, count in items.items():
            if item in self.inventory:
                self.inventory[item] += count
            else:
                self.inventory[item] = count

    def remove_items(self, item: str, quantity: int) -> bool:
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            return True
        return False

    def check_critical_threshold(self) -> Dict[str, bool]:
        return {item: count < self.critical_threshold for item, count in self.inventory.items()}

if __name__ == '__main__':
    manager = InventoryManager(critical_threshold=5)
    manager.add_items({"Apple": 10, "Banana": 3})
    print("Initial inventory:", manager.inventory)
    
    success = manager.remove_items("Apple", 2)
    print(f"Removed 2 apples: {success}")
    print("Inventory after removal:", manager.inventory)
    
    critical_items = manager.check_critical_threshold()
    print("Items below critical threshold:", critical_items)