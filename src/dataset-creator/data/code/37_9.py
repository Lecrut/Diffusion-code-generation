import logging
from datetime import datetime
from typing import Dict, List
class InventoryManager:
    def __init__(self) -> None:
        self.inventory: Dict[str, int] = {}
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    def add_item(self, item_id: str, quantity: int) -> None:
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer.")
        current_count = self.inventory.get(item_id, 0)
        new_quantity = current_count + quantity
        if new_quantity < 0:
            raise ValueError(f"Cannot reduce inventory of {item_id} below zero.")
        change_amount = new_quantity - current_count
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.inventory[item_id] = new_quantity
        log_message = f"[{timestamp}] Added {quantity} to item '{item_id}'. "\
                      f"Previous count: {current_count}, New count: {new_quantity}"
        self.logger.info(log_message)
    def remove_item(self, item_id: str, quantity: int) -> None:
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer.")
        current_count = self.inventory.get(item_id, 0)
        if quantity > current_count:
            raise ValueError(f"Cannot remove {quantity} from '{item_id}'. "\
                           f"Only {current_count} available.")
        change_amount = -quantity
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.inventory[item_id] = current_count + quantity
        log_message = f"[{timestamp}] Removed {quantity} from item '{item_id}'. "\
                      f"Previous count: {current_count}, New count: {self.inventory[item_id]}"
        self.logger.info(log_message)
    def update_batch(self, items_data: List[tuple]) -> None:
        for item_id, qty in items_data:
            if not isinstance(item_id, str):
                raise TypeError(f"Item ID must be a string, got {type(item_id)}")
            self.add_item(item_id, qty)
    def get_inventory_status(self) -> Dict[str, int]:
        return dict(sorted(self.inventory.items()))
if __name__ == '__main__':
    manager = InventoryManager()
    sample_batch = [
        ('WidgetA', 10),
        ('GadgetB', 5)
    ]
    manager.update_batch(sample_batch)
    manager.remove_item('WidgetA', 3)
    manager.add_item('GadgetC', 2)
    print("Final Inventory Status:")
    status = manager.get_inventory_status()
    for item, count in status.items():
        print(f"{item}: {count}")