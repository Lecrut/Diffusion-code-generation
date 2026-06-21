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
        if self.items[item_name] < quantity:
            return False
        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]
        return True

    def get_item_quantity(self, item_name):
        return self.items.get(item_name, 0)
if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.add_item('apple', 10)
    inventory.remove_item('apple', 3)
    print(inventory.get_item_quantity('apple'))