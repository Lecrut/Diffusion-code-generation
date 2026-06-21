from typing import Dict

class Item:
    def __init__(self, item_id: int, quantity: int):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Invalid item ID provided.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid quantity provided.")
        self.item_id = item_id
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items: Dict[int, Item] = {}

    def add_item(self, item: Item):
        if not isinstance(item, Item):
            raise ValueError("Invalid item type provided.")
        if item.item_id in self.items:
            self.items[item.item_id].quantity += item.quantity
        else:
            self.items[item.item_id] = item

    def get_item(self, item_id: int) -> Item:
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Invalid item ID provided.")
        if item_id in self.items:
            return self.items[item_id]
        else:
            raise KeyError(f"Item ID {item_id} not found.")

if __name__ == '__main__':
    inventory = Inventory()
    print("--- Testing Add Item ---")
    try:
        item1 = Item(1, 5)
        inventory.add_item(item1)
        print(inventory.get_item(1))
    except ValueError as e:
        print(e)
    except KeyError as e:
        print(e)