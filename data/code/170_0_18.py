class InventorySystem:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int):
            raise TypeError('Item name must be a string and quantity must be an integer.')
        if quantity <= 0:
            raise ValueError('Quantity must be a positive integer.')
        self.items[item_name] = self.items.get(item_name, 0) + quantity

    def remove_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int):
            raise TypeError('Item name must be a string and quantity must be an integer.')
        if quantity <= 0:
            raise ValueError('Quantity must be a positive integer.')
        if item_name not in self.items:
            raise KeyError(f"Item '{item_name}' not found in inventory.")
        if self.items[item_name] < quantity:
            raise ValueError(f'Not enough quantity of {item_name} to remove.')
        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]

    def get_item(self, item_name):
        if not isinstance(item_name, str):
            raise TypeError('Item name must be a string.')
        return self.items.get(item_name, 0)

    def update_quantity(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int):
            raise TypeError('Item name must be a string and quantity must be an integer.')
        if quantity <= 0:
            raise ValueError('Quantity must be a positive integer.')
        self.items[item_name] = quantity
if __name__ == '__main__':
    inventory = InventorySystem()
    inventory.add_item('apple', 10)
    print(inventory.get_item('apple'))
    inventory.remove_item('apple', 5)
    print(inventory.get_item('apple'))
    inventory.update_quantity('apple', 20)
    print(inventory.get_item('apple'))