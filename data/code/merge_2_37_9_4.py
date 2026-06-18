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
            raise ValueError(f"Cannot reduce stock of {item_id} below zero.")
        change_amount = new_quantity - current_count
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.inventory[item_id] = new_quantity
        log_message = f"[{timestamp}] Added/Updated item '{item_id}' by {change_amount} units. New total: {new_quantity}"
        self.logger.info(log_message)
    def remove_item(self, item_id: str, quantity: int) -> None:
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer.")
        current_count = self.inventory.get(item_id, 0)
        new_quantity = current_count - quantity
        if new_quantity < 0:
            raise ValueError(f"Cannot remove {quantity} units of '{item_id}'. Only {current_count} available.")
        change_amount = -quantity
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.inventory[item_id] = new_quantity
        log_message = f"[{timestamp}] Removed item '{item_id}' by {change_amount} units. New total: {new_quantity}"
        self.logger.info(log_message)
    def update_batch(self, items_data: List[tuple]) -> None:
        if not isinstance(items_data, list):
            raise TypeError("items_data must be a list.")
        valid_items = []
        invalid_items = []
        for item in items_data:
            if len(item) != 2 or not isinstance(item[0], str) or not isinstance(item[1], int):
                invalid_items.append(str(item))
                continue
            try:
                self.add_item(item[0], item[1])
                valid_items.append(item[0])
            except ValueError as ve:
                invalid_items.append(f"{item[0]} ({ve})")
        if not valid_items and not invalid_items:
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] Batch operation completed. Valid items updated: {valid_items}. Errors encountered with: {invalid_items}"
        self.logger.info(log_message)
    def get_inventory_status(self, item_id: str) -> int:
        return self.inventory.get(item_id, 0)
if __name__ == '__main__':
    manager = InventoryManager()
    sample_data = [
        ("Laptop", 5),
        ("Mouse", -10),
        ("Keyboard", 20),
        ("Monitor", -5),
        ("InvalidEntry", "not_a_number"), 
    ]
    manager.update_batch(sample_data)
    print(f"Current Laptop count: {manager.get_inventory_status('Laptop')}")