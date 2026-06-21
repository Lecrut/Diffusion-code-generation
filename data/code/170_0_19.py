class InventorySystem:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name: str, quantity: int) -> None:
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid input types. Item name must be a string and quantity must be a non-negative integer.')
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name: str, quantity: int) -> None:
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid input types. Item name must be a string and quantity must be a non-negative integer.')
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                raise ValueError(f'Error: Not enough quantity of {item_name} to remove.')
        else:
            raise KeyError(f'Error: {item_name} not found in inventory.')

    def get_item(self, item_name: str) -> int:
        if not isinstance(item_name, str):
            raise ValueError('Invalid input type. Item name must be a string.')
        return self.items.get(item_name, 0)

    def update_quantity(self, item_name: str, new_quantity: int) -> None:
        if not isinstance(item_name, str) or not isinstance(new_quantity, int) or new_quantity < 0:
            raise ValueError('Invalid input types. Item name must be a string and quantity must be a non-negative integer.')
        if item_name in self.items:
            self.items[item_name] = new_quantity
        else:
            raise KeyError(f'Error: {item_name} not found in inventory.')
if __name__ == '__main__':
    inventory = InventorySystem()
    inventory.add_item('apples', 10)
    print(inventory.get_item('apples'))
    inventory.remove_item('apples', 5)
    print(inventory.get_item('apples'))
    inventory.update_quantity('apples', 20)
    print(inventory.get_item('apples'))