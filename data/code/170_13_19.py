class Inventory:

    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, quantity):
        if item_id in self.items:
            self.items[item_id]['quantity'] += quantity
        else:
            self.items[item_id] = {'name': name, 'quantity': quantity}

    def remove_item(self, item_id, quantity):
        if item_id in self.items and self.items[item_id]['quantity'] >= quantity:
            self.items[item_id]['quantity'] -= quantity
            if self.items[item_id]['quantity'] == 0:
                del self.items[item_id]
            return True
        return False

    def get_stock_level(self, item_id):
        return self.items.get(item_id, {'name': 'Unknown', 'quantity': 0})['quantity']
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item(101, 'Laptop', 5)
    inventory.add_item(102, 'Mouse', 10)
    print(inventory.get_stock_level(101))
    print(inventory.remove_item(101, 3))
    print(inventory.get_stock_level(101))
    print(inventory.remove_item(103, 1))