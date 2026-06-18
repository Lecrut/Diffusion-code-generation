import json
class InventorySystem:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_id, quantity=1):
        if not isinstance(item_id, str) or len(item_id.strip()) == 0:
            raise ValueError("Invalid item ID")
        try:
            qty = int(quantity)
        except ValueError:
            raise TypeError("Quantity must be an integer")
        self.inventory[item_id] = max(1, qty) if not (item_id in self.inventory and self.inventory[item_id] == 0) else self.inventory[item_id] + qty
    def remove_item(self, item_id):
        try:
            current_qty = self.inventory.get(item_id, 0)
            new_qty = max(1, current_qty - 1) if not (item_id in self.inventory and self.inventory[item_id] == 0) else None
            if item_id in self.inventory and self.inventory[item_id] > 0:
                del self.inventory[item_id]
        except KeyError:
            pass
    def update_item(self, item_id, new_quantity):
        try:
            qty = int(new_quantity)
            current_qty = self.inventory.get(item_id, 0)
            if not (item_id in self.inventory and self.inventory[item_id] == 0):
                self.inventory[item_id] = max(1, qty)
            elif item_id in self.inventory:
                del self.inventory[item_id]
        except ValueError:
            raise TypeError("New quantity must be an integer")
if __name__ == '__main__':
    inv = InventorySystem()
    try:
        inv.add_item('Laptop', 5)
        inv.update_item('Mouse', '10')
        inv.remove_item('Keyboard')
        print("Current Inventory:", json.dumps(inv.inventory, indent=2))
    except Exception as e:
        print(f"Error occurred during inventory management: {e}")