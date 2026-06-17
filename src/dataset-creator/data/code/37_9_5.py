import logging
from datetime import datetime
from typing import Dict, List, Optional
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
        old_value = current_count
        self.inventory[item_id] = new_quantity
        change_message = (f"{datetime.now().isoformat()} - "
                         f"Inventory update for '{item_id}'. "
                         f"Old count: {old_value}, New count: {new_quantity}.")
        if old_value != 0 and quantity > 0:
            self.logger.info(change_message)
        elif new_quantity == 0:
            self.logger.warning(f"{datetime.now().isoformat()} - "
                              f"Inventory cleared for '{item_id}'.")
    def update_batch(self, item_ids: List[str], quantities: Dict[str, int]) -> None:
        if not isinstance(item_ids, list) or len(item_ids) != len(quantities):
            raise ValueError("Item IDs and quantities must be lists of the same length.")
        for i in range(len(item_ids)):
            item_id = item_ids[i]
            quantity = quantities.get(item_id, 0)
            if not isinstance(quantity, int):
                raise ValueError(f"Quantity for {item_id} is not an integer.")
            current_count = self.inventory.get(item_id, 0)
            try:
                old_value = current_count
                new_quantity = current_count + quantity
                if new_quantity < 0:
                    raise ValueError(
                        f"Cannot reduce inventory of '{item_id}' below zero. "
                        f"Requested change would result in negative stock."
                    )
                self.inventory[item_id] = new_quantity
                timestamp_str = datetime.now().isoformat()
                if old_value != 0 and quantity > 0:
                    msg = (f"{timestamp_str} - Inventory update for '{item_id}'. "
                           f"Old count: {old_value}, New count: {new_quantity}.")
                    self.logger.info(msg)
                elif new_quantity == 0:
                    msg = (f"{timestamp_str} - Inventory cleared for '{item_id}'.")
                    self.logger.warning(msg)
            except ValueError as ve:
                raise ve from None
if __name__ == '__main__':
    manager = InventoryManager()
    sample_items = ["Item-A", "Item-B", "Item-C"]
    sample_quantities = {"Item-A": 10, "Item-B": -5, "Item-C": 20}
    try:
        manager.update_batch(sample_items, sample_quantities)
        print("Current Inventory Status:")
        for item_id in sorted(manager.inventory.keys()):
            count = manager.inventory[item_id]
            status_msg = f"{item_id}: {count}" if count > 0 else f"{item_id}: Empty"
            print(f"- {status_msg}")
    except ValueError as e:
        print(f"Error occurred during batch update: {e}")