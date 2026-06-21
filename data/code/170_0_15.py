class InventorySystem:

    def __init__(self):
        self.items = {}

    @staticmethod
    def validate_item_name(item_name):
        if not isinstance(item_name, str) or not item_name:
            raise ValueError('Item name must be a non-empty string')

    @staticmethod
    def validate_quantity(quantity):
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Quantity must be a non-negative integer')

    def add_item(self, item_name, quantity):
        self.validate_item_name(item_name)
        self.validate_quantity(quantity)
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        self.validate_item_name(item_name)
        self.validate_quantity(quantity)
        if item_name not in self.items:
            raise KeyError(f'Item {item_name} not found in inventory')
        if self.items[item_name] < quantity:
            raise ValueError(f'Not enough quantity of {item_name} to remove')
        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]

    def get_item(self, item_name):
        self.validate_item_name(item_name)
        return self.items.get(item_name, 0)

    def update_quantity(self, item_name, new_quantity):
        self.validate_item_name(item_name)
        self.validate_quantity(new_quantity)
        if item_name in self.items:
            self.items[item_name] = new_quantity
        else:
            raise KeyError(f'Item {item_name} not found in inventory')
if __name__ == '__main__':
    inventory = InventorySystem()
    inventory.add_item('apple', 10)
    print(inventory.get_item('apple'))
    inventory.remove_item('apple', 5)
    print(inventory.get_item('apple'))
    inventory.update_quantity('apple', 20)
    print(inventory.get_item('apple'))