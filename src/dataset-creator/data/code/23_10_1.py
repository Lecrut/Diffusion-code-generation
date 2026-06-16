import json
def validate_input(item_name: str) -> bool:
    return item_name and not any(c in item_name for c in " \t\n\r")
class InventoryManager:
    def __init__(self):
        self.inventory = {}
    def add_item(self, name: str, quantity: int) -> None:
        if validate_input(name):
            try:
                qty = int(quantity)
                if qty < 0:
                    raise ValueError("Quantity must be non-negative.")
                self.inventory[name] = qty
            except ValueError as e:
                print(f"Invalid quantity for item '{name}': {e}")
    def get_quantity(self, name: str) -> int | None:
        return self.inventory.get(name) if validate_input(name) else None
if __name__ == '__main__':
    manager = InventoryManager()
    sample_data = [
        ("Apple", "10"),
        ("Banana", "5"),
        ("Cherry", "-3")                         
    ]
    for name, qty_str in sample_data:
        try:
            manager.add_item(name, qty_str)
        except ValueError as e:
            print(f"Error processing {name}: {e}")
    print("Current Inventory:")
    for item, count in sorted(manager.inventory.items()):
        print(f"{item}: {count}")