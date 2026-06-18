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
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        current_quantity = self.inventory.get(item_id, 0)
        new_quantity = current_quantity + int(quantity)
        old_value = current_quantity
        self.inventory[item_id] = new_quantity
        if old_value != new_quantity:
            change_msg = f"Item '{item_id}' count changed from {old_value} to {new_quantity}"
            self.logger.info(change_msg)
    def remove_item(self, item_id: str, quantity: int) -> None:
        current_quantity = self.inventory.get(item_id, 0)
        if not isinstance(quantity, (int, float)) or quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        if quantity > current_quantity:
            raise ValueError(f"Insufficient stock for item '{item_id}'.")
        old_value = current_quantity
        new_quantity = max(0, int(quantity) - current_quantity)
        self.inventory[item_id] = new_quantity
        if old_value != 0 and new_quantity < old_value:
            change_msg = f"Item '{item_id}' count reduced from {old_value} to {new_quantity}"
            self.logger.info(change_msg)
    def update_batch(self, items: List[tuple]) -> None:
        for item_id, qty in items:
            try:
                if isinstance(qty, float):
                    self.add_item(item_id, int(qty))
                else:
                    self.remove_item(item_id, int(qty))
            except ValueError as e:
                self.logger.error(f"Error processing {item_id}: {e}")
    def get_stock(self) -> Dict[str, int]:
        return dict(self.inventory)
if __name__ == '__main__':
    manager = InventoryManager()
    sample_operations = [
        ("Laptop", 10),
        ("Mouse", 50),
        ("Keyboard", 25),
        ("Monitor", 30),
        ("USB-Cable", 100)
    ]
    manager.update_batch(sample_operations)
    print("Current Inventory:")
    for item, count in sorted(manager.get_stock().items()):
        print(f"{item}: {count}")