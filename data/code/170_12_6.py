from typing import Dict

class Inventory:
    def __init__(self) -> None:
        self.items: Dict[str, int] = {}

    def add_item(self, item: str, quantity: int) -> None:
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def update_quantity(self, item: str, quantity: int) -> None:
        if item in self.items:
            self.items[item] += quantity
        else:
            raise ValueError(f"Item {item} not found")

    def remove_item(self, item: str, quantity: int) -> None:
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            if self.items[item] == 0:
                del self.items[item]
        else:
            raise ValueError(f"Insufficient stock for {item}")

    def get_stock(self, item: str) -> int:
        return self.items.get(item, 0)

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item("apple", 10)
    inventory.update_quantity("apple", 5)
    inventory.remove_item("apple", 3)
    print(inventory.get_stock("apple"))