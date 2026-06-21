class Inventory:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name not in self.items:
            self.items[item_name] = quantity
        else:
            self.items[item_name] += quantity
        return self

    def remove_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
        return self

    def get_quantity(self, item_name):
        return self.items.get(item_name, 0)
if __name__ == '__main__':
    inventory = Inventory()
    initial_inventory = {'apple': 10, 'banana': 5, 'orange': 12}
    print(f'Initial inventory: {initial_inventory}')
    updated_inventory = inventory.add_item('apple', 5).remove_item('banana', 3)
    final_inventory = (inventory.get_quantity('apple'), inventory.get_quantity('banana'), inventory.get_quantity('orange'))
    print(f'Updated inventory (apple, banana, orange): {final_inventory}')