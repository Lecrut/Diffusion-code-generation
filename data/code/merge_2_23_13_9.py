from typing import Dict
class Inventory:
    def __init__(self) -> None:
        self._items: Dict[str, int] = {}
    def add_item(self, name: str, quantity: int) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(quantity, (int, float)) or quantity < 0:
            raise ValueError("Quantity must be a non-negative number.")
        self._items[name] = int(self._items.get(name, 0) + quantity)
        return True
    def remove_item(self, name: str, quantity: int) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(quantity, (int, float)) or quantity < 0:
            raise ValueError("Quantity to remove must be a non-negative number.")
        current_qty = self._items.get(name, 0)
        if quantity > current_qty:
            return False
        new_quantity = int(current_qty - quantity)
        if new_quantity == 0:
            del self._items[name]
        else:
            self._items[name] = new_quantity
        return True
    def get_item(self, name: str) -> int | None:
        return self._items.get(name)
if __name__ == '__main__':
    inventory = Inventory()
    sample_items = [
        ("Apple", 5),
        ("Banana", 10),
        ("Orange", 3),
        ("Milk", 2.5),
    ]
    for name, qty in sample_items:
        inventory.add_item(name, qty)
    print("Initial Inventory:")
    for item_name, quantity in sorted(inventory._items.items()):
        if isinstance(quantity, float):
            print(f"{item_name}: {quantity:.1f}")
        else:
            print(f"{item_name}: {quantity}")
    inventory.remove_item("Banana", 3)
    print("\nUpdated Inventory:")
    for item_name, quantity in sorted(inventory._items.items()):
        if isinstance(quantity, float):
            print(f"{item_name}: {quantity:.1f}")
        else:
            print(f"{item_name}: {quantity}")
    retrieved = inventory.get_item("Apple")
    print(f"\nRetrieved Apple quantity: {retrieved}")