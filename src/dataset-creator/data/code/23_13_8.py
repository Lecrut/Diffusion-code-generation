from typing import Dict, List
class Inventory:
    def __init__(self) -> None:
        self._items: Dict[str, int] = {}
    def add_item(self, name: str, quantity: int) -> None:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        self._items[name] = quantity
    def get_quantity(self, name: str) -> int:
        return self._items.get(name, 0)
    def remove_item(self, name: str) -> None:
        if name in self._items:
            del self._items[name]
        else:
            raise KeyError(f"Item '{name}' not found.")
    def list_items(self) -> List[str]:
        return list(self._items.keys())
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("Laptop", 5)
    inventory.add_item("Mouse", 10)
    print(f"Quantity of Laptop: {inventory.get_quantity('Laptop')}")
    print(inventory.list_items())