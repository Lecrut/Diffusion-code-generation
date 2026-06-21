class InventorySystem:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name: str, quantity: int) -> None:
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid input')
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name: str, quantity: int) -> None:
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid input')
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                print(f'Error: Not enough quantity of {item_name} to remove.')
        else:
            print(f'Error: {item_name} not found in inventory.')

    def get_item(self, item_name: str) -> int:
        if not isinstance(item_name, str):
            raise ValueError('Invalid input')
        return self.items.get(item_name, 0)

    def update_quantity(self, item_name: str, quantity: int) -> None:
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid input')
        if item_name in self.items:
            self.items[item_name] = quantity
        else:
            print(f'Error: {item_name} not found in inventory.')
if __name__ == '__main__':
    inventory = InventorySystem()
    inventory.add_item('apple', 10)
    inventory.add_item('banana', 5)
    print(inventory.get_item('apple'))
    inventory.remove_item('apple', 3)
    print(inventory.get_item('apple'))
    inventory.update_quantity('banana', 2)
    print(inventory.get_item('banana'))