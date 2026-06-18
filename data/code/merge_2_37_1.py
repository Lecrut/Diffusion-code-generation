class InventorySystem:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_id, quantity=1):
        if not isinstance(item_id, str) or not isinstance(quantity, int):
            raise ValueError("Item ID must be a string and quantity must be an integer.")
        try:
            qty = max(0, quantity)
        except TypeError:
            raise ValueError("Quantity must be convertible to an integer.")
        if item_id in self.inventory:
            current_qty = self.inventory[item_id]
            new_total = current_qty + qty
            if new_total < 0:
                return False
            else:
                self.inventory[item_id] = new_total
                return True
        else:
            self.inventory[item_id] = qty
            return True
    def remove_item(self, item_id):
        if not isinstance(item_id, str):
            raise ValueError("Item ID must be a string.")
        if item_id in self.inventory and self.inventory[item_id] > 0:
            del self.inventory[item_id]
            return True
        else:
            return False
    def update_item(self, item_id, new_quantity):
        try:
            qty = int(new_quantity)
        except (ValueError, TypeError):
            raise ValueError("New quantity must be convertible to an integer.")
        if not isinstance(item_id, str):
            raise ValueError("Item ID must be a string.")
        current_qty = self.inventory.get(item_id, 0)
        try:
            new_total = int(current_qty + qty)
        except TypeError:
            return False
        if item_id in self.inventory and new_total < 0:
            return False
        else:
            self.inventory[item_id] = new_total
            return True
    def get_inventory(self):
        return dict(self.inventory)
if __name__ == '__main__':
    inv_system = InventorySystem()
    result1 = inv_system.add_item("Laptop", 5)
    print(f"Added Laptop: {result1}")
    result2 = inv_system.add_item("Mouse", 30)
    print(f"Added Mouse: {result2}")
    result3 = inv_system.update_item("Laptop", 2)
    print(f"Updated Laptop (+2): {result3}, Total: {inv_system.get_inventory().get('Laptop')}")
    result4 = inv_system.remove_item("Mouse")
    print(f"Removed Mouse: {result4}")
    result5 = inv_system.remove_item("NonExistentItem")
    print(f"Tried removing NonExistentItem: {result5}")
    print("\nFinal Inventory:")
    for k, v in inv_system.get_inventory().items():
        print(f"{k}: {v}")