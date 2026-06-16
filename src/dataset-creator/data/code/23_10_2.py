import re
def validate_quantity(value: str) -> bool:
    return value.isdigit() and int(value) > 0
class InventoryManager:
    def __init__(self):
        self.inventory = {}
    def add_item(self, item_name: str, quantity: str) -> None:
        if not re.match(r'^[a-zA-Z\s\-\'"]+$', item_name.strip()):
            raise ValueError("Item name must contain only alphanumeric characters and basic punctuation.")
        cleaned_quantity = quantity.strip()
        if not validate_quantity(cleaned_quantity):
            raise ValueError(f"Invalid quantity: {quantity}. Must be a positive integer.")
        self.inventory[item_name] = int(cleaned_quantity)
    def get_total_items(self) -> int:
        return sum(self.inventory.values())
if __name__ == '__main__':
    manager = InventoryManager()
    sample_data = [
        ("Apple", "10"),
        ("Banana", "5"),
        ("Orange", "3")
    ]
    for item, qty in sample_data:
        try:
            manager.add_item(item, qty)
        except ValueError as e:
            print(f"Error adding {item}: {e}")
    total = manager.get_total_items()
    print(f"Total items in inventory: {total}")