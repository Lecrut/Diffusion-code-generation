import logging
from datetime import datetime
class InventoryManager:
    def __init__(self):
        self.inventory = {}
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    def add_item(self, item_id: str, quantity: int):
        current_quantity = self.inventory.get(item_id, 0)
        new_quantity = current_quantity + quantity
        change_amount = new_quantity - current_quantity
        if change_amount != 0:
            old_value = f"{item_id}: {current_quantity}"
            new_value = f"{item_id}: {new_quantity}"
            self.logger.info("Count changed: %s -> %s", old_value, new_value)
        self.inventory[item_id] = new_quantity
    def update_batch(self, item_ids: list[str], quantities: dict):
        for item_id in item_ids:
            if item_id not in quantities:
                continue
            current_quantity = self.inventory.get(item_id, 0)
            new_quantity = current_quantity + quantities[item_id]
            change_amount = new_quantity - current_quantity
            if change_amount != 0:
                old_value = f"{item_id}: {current_quantity}"
                new_value = f"{item_id}: {new_quantity}"
                self.logger.info("Count changed: %s -> %s", old_value, new_value)
            self.inventory[item_id] = new_quantity
    def get_total_items(self):
        return sum(self.inventory.values())
if __name__ == '__main__':
    manager = InventoryManager()
    manager.add_item('A001', 50)
    manager.update_batch(['B002'], {'B002': 30})
    print(f"Total items: {manager.get_total_items()}")