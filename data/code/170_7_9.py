class Inventory:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += quantity
        return self

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
            return self
        else:
            raise ValueError('Not enough inventory to remove')

    def get_item_quantity(self, item_name):
        return self.items.get(item_name, 0)
if __name__ == '__main__':
    inventory = Inventory()
    print(f'Initial inventory: {inventory.items}')
    inventory.add_item('apple', 15).add_item('banana', 10)
    print(f'After adding items: {inventory.items}')
    inventory.remove_item('apple', 5)
    print(f'After removing 5 apples: {inventory.items}')
    try:
        inventory.remove_item('apple', 20)
    except ValueError as e:
        print(e)
    print(f'Final inventory: {inventory.items}')