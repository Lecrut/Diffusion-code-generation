from typing import Dict

class Inventory:

    def __init__(self):
        self.items: Dict[str, int] = {}

    def add_item(self, item_name: str, quantity: int) -> None:
        if not item_name or quantity < 0:
            raise ValueError('Invalid input')
        self.items[item_name] = self.items.get(item_name, 0) + quantity

    def update_quantity(self, item_name: str, quantity: int) -> None:
        if item_name not in self.items or quantity < 0:
            raise ValueError('Item not found or invalid quantity')
        self.items[item_name] = quantity

    def remove_item(self, item_name: str) -> None:
        if item_name not in self.items:
            raise ValueError('Item not found')
        del self.items[item_name]
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('apple', 10)
    inventory.update_quantity('apple', 5)
    inventory.remove_item('apple')
    print(inventory.items)