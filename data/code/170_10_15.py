class InventoryManager:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, (int, float)) or quantity < 0:
            raise ValueError('Invalid input')
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, (int, float)) or quantity < 0:
            raise ValueError('Invalid input')
        if item_name not in self.items:
            return False
        if self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
            return True
        else:
            return False

    def get_quantity(self, item_name):
        if not isinstance(item_name, str):
            raise ValueError('Invalid input')
        return self.items.get(item_name, 0)
if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.add_item('apples', 10)
    print(inventory.get_quantity('apples'))
    success = inventory.remove_item('apples', 5)
    print(success)
    print(inventory.get_quantity('apples'))
    success = inventory.remove_item('apples', 6)
    print(success)