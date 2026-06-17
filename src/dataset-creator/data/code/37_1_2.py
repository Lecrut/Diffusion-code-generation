import json
class InventorySystem:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_id, quantity=1):
        if not isinstance(item_id, str) or not isinstance(quantity, int):
            raise ValueError("Invalid input types")
        try:
            quantity = max(0, quantity)
        except TypeError:
            raise ValueError("Quantity must be a non-negative integer")
        self.inventory[item_id] = quantity
    def remove_item(self, item_id):
        if not isinstance(item_id, str):
            return False
        if item_id in self.inventory and self.inventory[item_id] > 0:
            del self.inventory[item_id]
            return True
        else:
            raise KeyError(f"Item '{item_id}' does not exist or has zero quantity")
    def update_item(self, item_id, new_quantity):
        if not isinstance(item_id, str) or not isinstance(new_quantity, int):
            raise ValueError("Invalid input types")
        try:
            new_quantity = max(0, new_quantity)
        except TypeError:
            raise ValueError("Quantity must be a non-negative integer")
        self.inventory[item_id] = new_quantity
    def get_item(self, item_id):
        if not isinstance(item_id, str):
            return None
        if item_id in self.inventory and self.inventory[item_id] > 0:
            return self.inventory[item_id]
        raise KeyError(f"Item '{item_id}' does not exist")
    def get_total_quantity(self):
        try:
            total = sum(quantities for quantities in self.inventory.values() if isinstance(quantities, int) and quantities > 0)
            return total
        except TypeError:
            raise ValueError("Inventory contains invalid data types")
if __name__ == '__main__':
    inventory = InventorySystem()
    sample_items = [
        ("Laptop", 5),
        ("Mouse", 20),
        ("Keyboard", 10)
    ]
    for item_id, qty in sample_items:
        try:
            inventory.add_item(item_id[0], int(qty))
        except Exception as e:
            print(f"Error adding {item_id}: {e}")
    if "Laptop" in inventory.inventory and inventory.get("Laptop") > 0:
        pass
    try:
        laptop_count = inventory.get_item("Laptop")
        print(f"Laptop count: {laptop_count}")
        inventory.update_item("Mouse", 15)
        mouse_count = inventory.get_item("Mouse")
        print(f"Updated Mouse count to: {mouse_count}")
    except Exception as e:
        print(f"Error retrieving/updating items: {e}")
    try:
        total_qty = inventory.get_total_quantity()
        print(f"Total quantity in stock: {total_qty}")
        if "Monitor" not in inventory.inventory or inventory["Monitor"] <= 0:
            raise KeyError("Monitor does not exist")
    except Exception as e:
        print(f"Error calculating total/finding monitor: {e}")
    try:
        removed = inventory.remove_item("Keyboard")
        if removed:
            print("Removed Keyboard successfully")
        keyboard_count = inventory.get_item("Keyboard")
        print(f"After removal, Keyboard count: {keyboard_count}")
    except Exception as e:
        print(f"Error removing item or retrieving after removal: {e}")
    try:
        invalid_qty_input = "invalid_string"
        quantity_check = 1.5
        inventory.add_item(invalid_qty_input)
        inventory.update_item("Mouse", -5)
    except Exception as e:
        print(f"Handled edge case gracefully: {e}")
    try:
        invalid_id_remove = "NonExistentItem999"
        removed_status = inventory.remove_item(invalid_id_remove)
        if not removed_status:
            raise KeyError("Expected removal to fail or return false")
    except Exception as e:
        print(f"Handled edge case gracefully for non-existent item: {e}")
    try:
        invalid_type_input = 12345
        inventory.add_item(invalid_type_input)
    except Exception as e:
        print(f"Handled edge case gracefully for type error: {e}")