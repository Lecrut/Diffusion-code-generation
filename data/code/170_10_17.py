class InventoryManager:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid input')
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid input')
        if item_name not in self.items:
            raise KeyError(f'{item_name} not found in inventory')
        if self.items[item_name] < quantity:
            raise ValueError(f'Not enough quantity of {item_name} to remove')
        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]

    def get_quantity(self, item_name):
        if not isinstance(item_name, str):
            raise ValueError('Invalid input')
        return self.items.get(item_name, 0)
if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.add_item('apple', 10)
    inventory.add_item('banana', 5)
    print(inventory.get_quantity('apple'))
    inventory.remove_item('apple', 3)
    print(inventory.get_quantity('apple'))
    try:
        inventory.remove_item('orange', 2)
    except KeyError as e:
        print(e)