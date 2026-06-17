from dataclasses import dataclass
from typing import List, Optional
@dataclass(frozen=True)
class InventoryItem:
    item_id: str
    name: str
    quantity: int
    def add_quantity(self, amount: int) -> "InventoryItem":
        return self.__class__(self.item_id, self.name, self.quantity + amount)
    def remove_quantity(self, amount: int) -> Optional["InventoryItem"]:
        new_qty = self.quantity - amount
        if new_qty < 0:
            return None
        return self.__class__(self.item_id, self.name, new_qty)
@dataclass(frozen=True)
class InventoryState:
    items: List[InventoryItem]
def calculate_total_value(state: InventoryState, price_map: dict[str, float]) -> float:
    total = 0.0
    for item in state.items:
        if item.item_id in price_map:
            total += item.quantity * price_map[item.item_id]
    return total
def get_low_stock_items(state: InventoryState, threshold: int) -> List[InventoryItem]:
    low_stock = []
    for item in state.items:
        if item.quantity < threshold:
            low_stock.append(item)
    return low_stock
if __name__ == '__main__':
    sample_prices = {
        "ITEM_001": 15.99,
        "ITEM_002": 24.50,
        "ITEM_003": 8.75
    }
    initial_items = [
        InventoryItem("ITEM_001", "Widget A", 10),
        InventoryItem("ITEM_002", "Gadget B", 3),
        InventoryItem("ITEM_003", "Tool C", 50)
    ]
    current_state = InventoryState(items=initial_items)
    updated_item_a = initial_items[0].remove_quantity(2) or initial_items[0]
    updated_item_b = initial_items[1].add_quantity(7) 
    new_state = InventoryState(items=[updated_item_a, updated_item_b])
    total_val = calculate_total_value(new_state, sample_prices)
    low_stock_list = get_low_stock_items(new_state, 5)
    print(f"Total Value: {total_val:.2f}")
    for item in low_stock_list:
        print(f"{item.name}: {item.quantity} units")