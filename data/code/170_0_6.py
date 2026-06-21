class InventorySystem:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name: str, quantity: int):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid item name or quantity')
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name: str, quantity: int):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid item name or quantity')
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
        else:
            raise ValueError('Not enough inventory')

    def get_item(self, item_name: str):
        if not isinstance(item_name, str):
            raise ValueError('Invalid item name')
        return self.items.get(item_name, 0)

    def update_quantity(self, item_name: str, quantity: int):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError('Invalid item name or quantity')
        if item_name in self.items:
            self.items[item_name] = quantity
        else:
            raise ValueError('Item does not exist')
if __name__ == '__main__':
    inventory = InventorySystem()
    inventory.add_item('apple', 10)
    print(inventory.get_item('apple'))
    inventory.remove_item('apple', 5)
    print(inventory.get_item('apple'))
    inventory.update_quantity('apple', 20)
    print(inventory.get_item('apple'))