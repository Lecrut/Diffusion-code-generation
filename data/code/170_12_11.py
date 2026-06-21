from typing import Dict

class Inventory:
    def __init__(self):
        self.items: Dict[str, int] = {}

    def add_item(self, item_name: str, quantity: int) -> None:
        if not item_name or not isinstance(quantity, int) or quantity < 0:
            return
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def update_quantity(self, item_name: str, quantity: int) -> None:
        if not item_name or not isinstance(quantity, int) or quantity < 0:
            return
        if item_name in self.items:
            self.items[item_name] = quantity
        else:
            raise ValueError(f"Item {item_name} not found")

    def remove_item(self, item_name: str) -> None:
        if item_name in self.items:
            del self.items[item_name]
        else:
            raise ValueError(f"Item {item_name} not found")

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('apple', 10)
    print(inventory.items)
    inventory.update_quantity('apple', 20)
    print(inventory.items)
    inventory.remove_item('apple')
    try:
        print(inventory.items['apple'])
    except ValueError as e:
        print(e)