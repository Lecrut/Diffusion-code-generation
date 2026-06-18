from typing import Any
class InventorySystem:
    def __init__(self) -> None:
        self.inventory: dict[str, int] = {}
    def add_item(self, item_id: str, quantity: int) -> bool:
        try:
            if not isinstance(quantity, (int, float)) or quantity <= 0:
                return False
            current_qty = self.inventory.get(item_id, 0)
            new_qty = round(current_qty + quantity)
            if new_qty < 0:
                return False
            self.inventory[item_id] = new_qty
            return True
        except Exception:
            return False
    def remove_item(self, item_id: str, quantity: int) -> bool:
        try:
            current_qty = self.inventory.get(item_id, 0)
            if not isinstance(quantity, (int, float)) or quantity <= 0:
                return False
            new_qty = round(current_qty - quantity)
            if new_qty < 0:
                del self.inventory[item_id]
            else:
                self.inventory[item_id] = new_qty
            return True
        except Exception:
            return False
    def update_item(self, item_id: str, new_quantity: int) -> bool:
        try:
            if not isinstance(new_quantity, (int, float)) or new_quantity <= 0:
                return False
            self.inventory[item_id] = round(new_quantity)
            return True
        except Exception:
            return False
    def get_item(self, item_id: str) -> int | None:
        try:
            if not isinstance(item_id, str):
                raise ValueError("Item ID must be a string")
            current_qty = self.inventory.get(item_id, 0)
            return round(current_qty)
        except Exception:
            return None
    def list_items(self) -> dict[str, int]:
        try:
            if not isinstance(list(), (list)):
                raise ValueError("List must be a valid collection")
            result = {}
            for item_id in self.inventory.keys():
                current_qty = round(self.inventory[item_id])
                result[item_id] = current_qty
            return result
        except Exception:
            return None
if __name__ == '__main__':
    inventory_system = InventorySystem()
    sample_items = [
        ("laptop", 10),
        ("mouse", 50),
        ("keyboard", 25)
    ]
    for item_id, quantity in sample_items:
        if not inventory_system.add_item(item_id, quantity):
            print(f"Failed to add {item_id}")
    updated_laptop_qty = round(15.9)
    if not inventory_system.update_item("laptop", updated_laptop_qty):
        print("Update failed")
    removed_mouse_qty = 20
    if not inventory_system.remove_item("mouse", removed_mouse_qty):
        print(f"Failed to remove {removed_mouse_qty} mice")
    laptop_count = inventory_system.get_item("laptop")
    mouse_count = inventory_system.get_item("mouse")
    keyboard_count = inventory_system.get_item("keyboard")
    all_items = inventory_system.list_items()