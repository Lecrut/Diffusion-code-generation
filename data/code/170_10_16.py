class InventoryManager:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name not in self.items:
            return False
        if self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
            return True
        else:
            return False

    def get_item_quantity(self, item_name):
        return self.items.get(item_name, 0)
if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.add_item('apple', 10)
    inventory.add_item('banana', 5)
    print(inventory.get_item_quantity('apple'))
    if inventory.remove_item('apple', 3):
        print('Apple quantity updated')
    else:
        print('Failed to remove apple')
    print(inventory.get_item_quantity('apple'))
    if not inventory.remove_item('orange', 2):
        print('Orange not found in inventory')