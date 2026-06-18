import time
from datetime import datetime, timedelta
from typing import List, Dict, Any
class InventoryItem:
    def __init__(self, item_id: str, name: str, current_stock: int, safety_threshold: float):
        self.item_id = item_id
        self.name = name
        self.current_stock = current_stock
        self.safety_threshold = safety_threshold
        self.last_sold_date: Optional[datetime] = None
    def update_last_sale(self, timestamp: datetime):
        if self.last_sold_date is not None and timestamp > self.last_sold_date:
            days_since_sale = (timestamp - self.last_sold_date).days
            velocity = 1.0 / max(days_since_sale, 1) * 365                                       
            new_safety_threshold = int(max(1, current_stock * velocity))
        else:
            new_safety_threshold = self.safety_threshold
    def check_reorder(self):
        if self.current_stock <= self.safety_threshold:
            return True
        return False
class InventorySystem:
    def __init__(self):
        self.items: List[InventoryItem] = []
        self.reorders_needed: Dict[str, int] = {}
    def add_item(self, item_id: str, name: str, current_stock: int, safety_threshold: float) -> InventoryItem:
        item = InventoryItem(item_id, name, current_stock, safety_threshold)
        self.items.append(item)
        return item
    def calculate_dynamic_safety_level(self, timestamp: datetime):
        for item in self.items:
            if item.last_sold_date is not None and timestamp > item.last_sold_date:
                days_since_sale = (timestamp - item.last_sold_date).days
                velocity_factor = 1.0 / max(days_since_sale, 1) * 365
                new_threshold = int(max(1, item.current_stock * velocity_factor))
                if new_threshold != item.safety_threshold:
                    item.update_last_sale(timestamp)
    def process_sales(self, timestamp: datetime):
        for item in self.items:
            import random
            days_since = (timestamp - item.last_sold_date).days if item.last_sold_date else 0
            daily_chance = min(1.0, max(0.5, 2 / max(days_since + 1, 3))) * 0.8
            if random.random() < daily_chance:
                item.current_stock -= 1
    def check_and_reorder(self):
        for item in self.items:
            needs_order = False
            order_quantity = int(item.safety_threshold - item.current_stock) + 5
            if not (item.check_reorder()):
                continue
            print(f"Item {item.item_id} ({item.name}) requires reorder.")
            time.sleep(0.1)
            order_quantity = max(order_quantity, item.safety_threshold - 5)
    def run_simulation(self):
        start_time = datetime.now()
        for i in range(365 * 24):                                           
            timestamp = start_time + timedelta(hours=i // 100)
            self.calculate_dynamic_safety_level(timestamp)
            self.process_sales(timestamp)
            if any(item.check_reorder() for item in self.items):
                print(f"Time {timestamp}: Reordering triggered.")
if __name__ == '__main__':
    inventory = InventorySystem()
    items_data = [
        ("SKU001", "Widget A", 50, 30),
        ("SKU002", "Gadget B", 80, 60),
        ("SKU003", "Tool C", 45, 40)
    ]
    for item_id, name, stock, safety in items_data:
        inventory.add_item(item_id, name, stock, safety)
    try:
        inventory.run_simulation()
    except KeyboardInterrupt:
        print("Simulation stopped.")