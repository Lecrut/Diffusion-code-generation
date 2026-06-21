class InventorySystem:
    MIN_QUANTITY = 0

    def __init__(self):
        self.items = {}

    @staticmethod
    def validate_quantity(quantity):
        if not isinstance(quantity, int) or quantity < InventorySystem.MIN_QUANTITY:
            raise ValueError('Quantity must be a non-negative integer')

    def add_item(self, item_name, quantity):
        InventorySystem.validate_quantity(quantity)
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        InventorySystem.validate_quantity(quantity)
        if item_name not in self.items:
            raise KeyError(f'{item_name} not found in inventory')
        if self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
        else:
            raise ValueError(f'Not enough quantity of {item_name} to remove')

    def get_item(self, item_name):
        return self.items.get(item_name, 0)

    def update_quantity(self, item_name, quantity):
        InventorySystem.validate_quantity(quantity)
        if item_name not in self.items:
            raise KeyError(f'{item_name} not found in inventory')
        self.items[item_name] = quantity
if __name__ == '__main__':
    inventory = InventorySystem()
    inventory.add_item('apple', 10)
    print(inventory.get_item('apple'))
    inventory.remove_item('apple', 5)
    print(inventory.get_item('apple'))
    inventory.update_quantity('apple', 20)
    print(inventory.get_item('apple'))