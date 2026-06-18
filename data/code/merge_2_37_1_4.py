class InventorySystem:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_id, quantity=1):
        if not isinstance(item_id, str) or not isinstance(quantity, int):
            raise ValueError("Invalid input types. item_id must be a string and quantity an integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.inventory[item_id] = quantity
    def remove_item(self, item_id):
        if item_id not in self.inventory:
            print(f"Item '{item_id}' not found in inventory.")
            return False
        del self.inventory[item_id]
        return True
    def update_quantity(self, item_id, new_quantity):
        if isinstance(new_quantity, int) and new_quantity > 0:
            old_qty = self.inventory.get(item_id, 0)
            diff = new_quantity - old_qty
            if diff < 0:
                print(f"Insufficient quantity for '{item_id}'. Current stock: {old_qty}.")
                return False
        else:
            raise ValueError("New quantity must be a positive integer.")
        self.inventory[item_id] = new_quantity
    def get_item(self, item_id):
        if item_id in self.inventory:
            print(f"Item '{item_id}' is available. Quantity: {self.inventory[item_id]}")
            return True
        else:
            print(f"Item '{item_id}' not found.")
            return False
    def list_all_items(self):
        if len(self.inventory) == 0:
            print("Inventory is empty.")
        for item, qty in self.inventory.items():
            print(f"{item}: {qty}")
if __name__ == '__main__':
    inv = InventorySystem()
    try:
        inv.add_item('Laptop', 5)
        inv.add_item('Mouse', 20)
        inv.add_item('Keyboard', 15)
        print("--- Initial List ---")
        inv.list_all_items()
        result = inv.update_quantity('Mouse', 30)
        if not result:
            pass
        print("\n--- Updated List ---")
        inv.list_all_items()
        try:
            inv.remove_item('Monitor')
        except KeyError as e:
            print(f"Error during removal: {e}")
        if 'Keyboard' in inv.inventory:
            inv.remove_item('Keyboard')
        print("\n--- Final List ---")
        inv.list_all_items()
    except ValueError as ve:
        print(f"Validation Error: {ve}")