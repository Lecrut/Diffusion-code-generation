import json
def validate_input(item_name: str) -> bool:
    return isinstance(item_name, str) and item_name.strip() != ""
class InventoryManager:
    def __init__(self):
        self.inventory = {}
    def add_item(self, name: str, quantity: int) -> None:
        if not validate_input(name):
            raise ValueError("Item name must be a non-empty string.")
        try:
            qty = int(quantity)
            if qty < 0:
                raise ValueError(f"Quantity {quantity} cannot be negative.")
            self.inventory[name] = qty
        except (ValueError, TypeError):
            raise ValueError("Invalid quantity. Must be a non-negative integer.")
    def get_quantity(self, name: str) -> int | None:
        if not validate_input(name):
            return None
        return self.inventory.get(name.strip())
if __name__ == '__main__':
    manager = InventoryManager()
    sample_items = [
        ("Apple", 5),
        ("Banana", 12),
        ("Orange", -3)
    ]
    for name, qty in sample_items:
        try:
            manager.add_item(name, qty)
        except ValueError as e:
            print(f"Error adding {name}: {e}")
    valid_names = ["Apple", "Banana"]
    results = {}
    for n in valid_names:
        q = manager.get_quantity(n)
        if q is not None:
            results[n] = f"{q} units available."
        else:
            results[n] = "Item not found or invalid input detected during retrieval check."
    print(json.dumps(results, indent=2))