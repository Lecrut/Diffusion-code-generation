from dataclasses import dataclass, field
from typing import Dict, List
@dataclass(frozen=True)
class InventoryItem:
    id: str
    name: str
    quantity: int = 0
    def add_quantity(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Quantity cannot be decreased via this method.")
        self.quantity += amount
    def remove_quantity(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Quantity cannot be decreased via this method.")
        self.quantity -= amount
    def __repr__(self) -> str:
        return f"InventoryItem(id={self.id}, name='{self.name}', quantity={self.quantity})"
class InventoryManager:
    def __init__(self, initial_items: List[Dict[str, any]] = None) -> None:
        self._items: Dict[str, InventoryItem] = {}
        if initial_items is not None:
            for item_data in initial_items:
                qty = item_data.get('quantity', 0)
                self.add_item(item_data['id'], item_data['name'], qty)
    def add_item(self, id: str, name: str, quantity: int = 0) -> InventoryItem:
        self._items[id] = InventoryItem(id=id, name=name, quantity=quantity)
        return self._items[id]
    def get_item(self, id: str) -> InventoryItem | None:
        return self._items.get(id)
    def update_quantity(self, id: str, amount: int = 0) -> bool:
        item = self.get_item(id)
        if item is None:
            return False
        try:
            new_qty = item.quantity + amount
            if new_qty < 0:
                raise ValueError(f"Cannot reduce stock of '{item.name}' to negative value.")
            item.quantity = new_qty
            return True
        except Exception as e:
            print(f"Error updating quantity for {id}: {e}")
            return False
    def get_all_items(self) -> List[InventoryItem]:
        return list(self._items.values())
if __name__ == '__main__':
    initial_stock = [
        {'id': 'ITEM-001', 'name': 'Widget A'},
        {'id': 'ITEM-002', 'name': 'Gadget B', 'quantity': 50},
        {'id': 'ITEM-003', 'name': 'Tool C'}
    ]
    manager = InventoryManager(initial_stock)
    print("Initial State:")
    for item in manager.get_all_items():
        print(f"  {item}")
    widget_a_id = 'ITEM-001'
    manager.update_quantity(widget_a_id, amount=25)
    gadget_b_id = 'ITEM-002'
    manager.update_quantity(gadget_b_id, amount=-5)
    print("\nUpdated State:")
    for item in manager.get_all_items():
        print(f"  {item}")
    retrieved_item = manager.get_item('ITEM-003')
    if retrieved_item:
        print(f"\nRetrieved Item Details - ID: {retrieved_item.id}, Name: {retrieved_item.name}, Count: {retrieved_item.quantity}")