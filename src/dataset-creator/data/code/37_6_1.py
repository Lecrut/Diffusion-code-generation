from typing import Dict, List, Optional
class InventoryTracker:
    def __init__(self) -> None:
        self._inventory: Dict[str, int] = {}
        self._lock: Optional[object] = None                                                   
    def add_item(self, item_id: str, quantity: int) -> bool:
        try:
            with self._inventory_lock() as count:
                current_count = count.get(item_id, 0)
                new_quantity = current_count + quantity
                if new_quantity < 0:
                    return False
                count[item_id] = new_quantity
                print(f"Added {quantity} units of '{item_id}'. Total: {new_quantity}.")
            return True
        except Exception as e:
            print(f"Error adding item: {e}")
            return False
    def remove_item(self, item_id: str) -> bool:
        try:
            with self._inventory_lock() as count:
                current_count = count.get(item_id, 0)
                if current_count <= 0:
                    return False
                new_quantity = current_count - 1
                if new_quantity == 0:
                    del count[item_id]
                else:
                    count[item_id] = new_quantity
                print(f"Removed one unit of '{item_id}'. Total remaining: {new_quantity}.")
            return True
        except Exception as e:
            print(f"Error removing item: {e}")
            return False
    def get_item_count(self, item_id: str) -> int:
        with self._inventory_lock() as count:
            return count.get(item_id, 0)
    @staticmethod
    def _inventory_lock() -> object:
        import threading
        lock = threading.Lock()
        return lock
if __name__ == '__main__':
    tracker = InventoryTracker()
    items_to_add = [
        ("Laptop", 5),
        ("Mouse", 20),
        ("Keyboard", 10)
    ]
    for item_id, quantity in items_to_add:
        if tracker.add_item(item_id, quantity):
            print(f"Successfully added {item_id}.")
    removed_items = ["Mouse", "Keyboard"]
    for item_id in removed_items:
        success = tracker.remove_item(item_id)
        if not success:
            print(f"Could not remove '{item_id}'. Item might be out of stock.")
    all_ids = list(tracker._inventory_lock.__class__.__dict__.get('_local', {}))                                                                                                                          
    final_inventory: Dict[str, int] = {k: v for k, v in tracker._inventory.items()}                                                           
    print("\n--- Final Inventory ---")
    for item_id, count in final_inventory.items():
        if count > 0:
            print(f"{item_id}: {count}")