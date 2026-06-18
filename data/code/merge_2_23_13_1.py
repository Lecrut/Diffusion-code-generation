from typing import List, Dict
class Inventory:
    def __init__(self) -> None:
        self._items: Dict[str, int] = {}
    def add_item(self, name: str, quantity: int) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        self._items[name] = quantity
    def remove_item(self, name: str) -> bool:
        return self._items.pop(name, None) is not None
    def get_total_items(self) -> int:
        return sum(self._items.values())
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("Apple", 10)
    inventory.add_item("Banana", 5)
    print(f"Total items in inventory: {inventory.get_total_items()}")