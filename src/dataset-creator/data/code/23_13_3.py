from typing import List, Dict
class Inventory:
    def __init__(self) -> None:
        self._items: List[Dict[str, int]] = []
    def add_item(self, name: str, quantity: int) -> bool:
        if not isinstance(name, str):
            raise TypeError("Item name must be a string.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        for item in self._items:
            if item["name"] == name:
                existing_quantity = item["quantity"] + quantity
                return True
        new_item = {"name": name, "quantity": quantity}
        self._items.append(new_item)
        return False
    def get_inventory(self) -> List[Dict[str, int]]:
        return list(self._items)
if __name__ == '__main__':
    inventory = Inventory()
    sample_items = [
        ("Apple", 10),
        ("Banana", 5),
        ("Orange", 20),
        ("Grapes", 3)
    ]
    for name, quantity in sample_items:
        success = inventory.add_item(name, quantity)
        if not success:
            print(f"Item '{name}' already exists.")
    current_inventory = inventory.get_inventory()
    total_quantity = sum(item["quantity"] for item in current_inventory)
    print("Current Inventory:")
    for item in current_inventory:
        print(f"{item['name']}: {item['quantity']}")
    print(f"Total items: {total_quantity}")