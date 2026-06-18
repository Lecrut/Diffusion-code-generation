from typing import Dict
class Inventory:
    def __init__(self) -> None:
        self._items: Dict[str, int] = {}
    def add_item(self, name: str, quantity: int) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self._items[name] = quantity
        return True
    def get_quantity(self, name: str) -> int | None:
        return self._items.get(name)
    def remove_item(self, name: str) -> bool:
        if name in self._items:
            del self._items[name]
            return True
        return False
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("Laptop", 5)
    inventory.add_item("Mouse", 10)
    assert inventory.get_quantity("Laptop") == 5
    assert inventory.remove_item("Mouse") is True
    assert inventory.get_quantity("Mouse") is None