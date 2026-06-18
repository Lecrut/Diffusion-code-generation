import logging
from datetime import datetime
from typing import List, Dict
class InventoryManager:
    def __init__(self) -> None:
        self.inventory: Dict[str, int] = {}
        self.logger = logging.getLogger(__name__)
        self._setup_logging()
    def _setup_logging(self) -> None:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    def add_item(self, item_id: str, quantity: int) -> None:
        current_count = self.inventory.get(item_id, 0)
        new_quantity = current_count + quantity
        change_amount = new_quantity - current_count
        timestamp = datetime.now().isoformat()
        if change_amount > 0:
            message = f"Added {quantity} to item '{item_id}' (Total: {new_quantity}) at {timestamp}"
        elif change_amount < 0:
            message = f"Removed {-change_amount} from item '{item_id}' (Total: {abs(new_quantity)}) at {timestamp}"
        self.inventory[item_id] = new_quantity
        self.logger.info(message)
    def update_batch(self, items: List[Dict[str, int]]) -> None:
        for entry in items:
            item_id = entry['item_id']
            quantity_change = entry.get('quantity', 0)
            if not isinstance(quantity_change, (int, float)):
                continue
            current_count = self.inventory.get(item_id, 0)
            new_quantity = int(current_count + quantity_change)
            change_amount = new_quantity - current_count
            timestamp = datetime.now().isoformat()
            if change_amount > 0:
                message = f"Batch added {quantity_change} to item '{item_id}' (Total: {new_quantity}) at {timestamp}"
            elif change_amount < 0:
                message = f"Batch removed {-change_amount} from item '{item_id}' (Total: {abs(new_quantity)}) at {timestamp}"
            self.inventory[item_id] = new_quantity
            self.logger.info(message)
    def get_inventory(self) -> Dict[str, int]:
        return dict(self.inventory)
if __name__ == '__main__':
    manager = InventoryManager()
    sample_items: List[Dict[str, int]] = [
        {'item_id': 'SKU001', 'quantity': 5},
        {'item_id': 'SKU002', 'quantity': -3}
    ]
    manager.update_batch(sample_items)
    print(manager.get_inventory())