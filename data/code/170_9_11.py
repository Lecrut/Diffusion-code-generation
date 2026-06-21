CONVERSION_FACTOR = 1.0

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            self.items[item_id]['quantity'] += quantity
            self.items[item_id]['price'] = price
        else:
            self.items[item_id] = {
                'name': name,
                'quantity': quantity,
                'price': price
            }

    def calculate_total_value(self):
        return sum(item['quantity'] * item['price'] for item in self.items.values())

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('001', 'Widget A', 10, 5.99)
    inventory.add_item('002', 'Widget B', 20, 3.49)
    print("Total Inventory Value:", inventory.calculate_total_value())