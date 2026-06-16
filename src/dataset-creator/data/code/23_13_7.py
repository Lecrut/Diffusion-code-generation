from typing import Dict, List
class Inventory:
    def __init__(self) -> None:
        self._items: Dict[str, int] = {}
    def add_item(self, name: str, quantity: int) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        self._items[name] = quantity
        return True
    def remove_item(self, name: str) -> bool:
        if name in self._items:
            del self._items[name]
            return True
        return False
    def get_quantity(self, name: str) -> int | None:
        return self._items.get(name)
    def list_items(self) -> List[str]:
        return list(self._items.keys())
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("Laptop", 5)
    inventory.add_item("Mouse", 10)
    print(f"Total items: {len(inventory.list_items())}")