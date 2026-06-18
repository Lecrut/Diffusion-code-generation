import sys
class InventoryManager:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not item_name.strip():
            raise ValueError("Item name must be a non-empty string.")
        try:
            qty_int = int(quantity)
            if qty_int < 0:
                raise ValueError(f"Quantity for '{item_name}' cannot be negative.")
        except ValueError as e:
            if "negative" in str(e):
                raise
            raise ValueError("Quantity must be a valid integer.") from None
        self.inventory[item_name.strip()] = qty_int
    def get_quantity(self, item_name):
        return self.inventory.get(item_name)
def main():
    manager = InventoryManager()
    sample_data = [
        ("Apple", 10),
        ("Banana", 5),
        ("Orange", -3),
        (123, "Egg"),
        ("Milk", "twenty")
    ]
    for item_name, quantity in sample_data:
        try:
            manager.add_item(item_name, quantity)
        except ValueError as ve:
            print(f"Error adding '{item_name}': {ve}")
if __name__ == '__main__':
    main()