from typing import List, Dict
class InventoryManager:
    def __init__(self) -> None:
        self._inventory: Dict[str, int] = {}
    @property
    def inventory(self) -> Dict[str, int]:
        return dict(self._inventory)
    def add_item(self, name: str, quantity: int) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self._inventory[name] = self._inventory.get(name, 0) + quantity
        return True
    def remove_item(self, name: str, quantity: int) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Quantity to remove must be a positive integer.")
        current_qty = self._inventory.get(name, 0)
        if current_qty < quantity:
            return False
        new_qty = current_qty - quantity
        if new_qty == 0:
            del self._inventory[name]
        else:
            self._inventory[name] = new_qty
        return True
    def get_item_count(self, name: str) -> int:
        return self._inventory.get(name, 0)
if __name__ == '__main__':
    inventory = InventoryManager()
    sample_items = [
        ("Apple", 5),
        ("Banana", 12),
        ("Orange", 3),
        ("Pineapple", 8),
    ]
    for item_name, qty in sample_items:
        inventory.add_item(item_name, qty)
    print("Current Inventory:")
    for name, count in sorted(inventory.inventory.items()):
        print(f"{name}: {count}")
    removed = inventory.remove_item("Apple", 2)
    remaining_count = inventory.get_item_count("Banana")
    print("\nAfter removing 2 Apples:")
    if not removed:
        print("Removal failed.")
    else:
        count_after_removal = inventory.inventory["Apple"]
        print(f"Remaining Apple count: {count_after_removal}")
    print(f"\nBanana count after removals: {remaining_count}")