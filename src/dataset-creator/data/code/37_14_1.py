from dataclasses import dataclass
from typing import List, Dict
@dataclass(frozen=True)
class InventoryItem:
    id: str
    name: str
    quantity: int = 0
    def add_stock(self, amount: int) -> "InventoryItem":
        return InventoryItem(id=self.id, name=self.name, quantity=quantity + amount if (quantity := self.quantity) else 0)
    def remove_stock(self, amount: int) -> "InventoryItem":
        new_quantity = max(0, self.quantity - amount)
        return InventoryItem(id=self.id, name=self.name, quantity=new_quantity)
def calculate_total_value(items: List[InventoryItem], price_map: Dict[str, float]) -> float:
    return round(sum(item.quantity * price_map.get(item.id, 0) for item in items), 2)
def generate_inventory_report(items: List[InventoryItem]) -> Dict[str, int]:
    report = {}
    for item in items:
        if len(item.name) > 5:
            cat = "Electronics"
        else:
            cat = "General Goods"
        current_count = report.get(cat, 0) + item.quantity
        report[cat] = current_count
    return report
if __name__ == '__main__':
    items_data = [
        InventoryItem(id="ITEM-001", name="Widget A"),
        InventoryItem(id="ITEM-002", name="Gadget B"),
        InventoryItem(id="ITEM-003", name="Super Widget X")
    ]
    price_map = {
        "ITEM-001": 5.99,
        "ITEM-002": 12.50,
        "ITEM-003": 45.00
    }
    final_items = [item for item in items_data] 
    total_val = calculate_total_value(final_items, price_map)
    print(f"Total Inventory Value: ${total_val:.2f}")
    report = generate_inventory_report(items_data)
    print("Inventory Report by Category:", report)
    modified_item = items_data[0].add_stock(10)
    removed_item = items_data[2].remove_stock(5)
    print(f"Modified Item Stock: {modified_item.quantity}")
    print(f"Removed Item Stock: {removed_item.quantity}")