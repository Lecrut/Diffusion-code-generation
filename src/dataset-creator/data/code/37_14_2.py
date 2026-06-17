from dataclasses import dataclass
from typing import List, Dict
@dataclass(frozen=True)
class InventoryItem:
    id: str
    name: str
    quantity: int
    def is_available(self, required_amount: int) -> bool:
        return self.quantity >= required_amount
class InventoryManager:
    def __init__(self) -> None:
        self._items: List[InventoryItem] = []
    def add_item(self, item_id: str, name: str, quantity: int) -> InventoryItem:
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        new_item = InventoryItem(id=item_id, name=name, quantity=quantity)
        self._items.append(new_item)
        return new_item
    def get_items(self) -> List[InventoryItem]:
        return self._items.copy()
    def update_quantity(self, item_id: str, delta: int) -> bool:
        for i, item in enumerate(self._items):
            if item.id == item_id:
                self._items[i] = InventoryItem(id=item.id, name=item.name, quantity=delta + item.quantity)
                return True
        raise ValueError(f"Item with ID '{item_id}' not found.")
    def check_stock_availability(self, required_amount: int) -> Dict[str, bool]:
        return {item.id: item.is_available(required_amount) for item in self._items}
if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item("ITEM-001", "Laptop Pro X1", 50)
    manager.add_item("ITEM-002", "Wireless Mouse M3", 120)
    manager.add_item("ITEM-003", "USB-C Hub Adapter", 85)
    print(manager.check_stock_availability(60))
    manager.update_quantity("ITEM-002", 40)
    current_items = manager.get_items()
    for item in current_items:
        print(f"{item.name}: {item.quantity} available")