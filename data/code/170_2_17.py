from collections import defaultdict

class Inventory:
    def __init__(self):
        self.items = defaultdict(int)
    
    def add_items(self, items):
        for item_id, quantity in items.items():
            if self.items[item_id] > 0:
                raise ValueError(f"Item ID {item_id} already exists in the inventory.")
            self.items[item_id] += quantity
    
    def calculate_total_value(self, prices):
        return sum(quantity * price for item_id, (quantity, price) in self.items.items() if item_id in prices)

if __name__ == '__main__':
    my_inventory = Inventory()
    items_to_add = {101: 50, 102: 30}
    try:
        my_inventory.add_items(items_to_add)
        print("Items added successfully.")
    except ValueError as e:
        print(f"Error: {e}")
    
    prices = {101: 1.0, 102: 0.5}
    total_value = my_inventory.calculate_total_value(prices)
    print(f"Total inventory value: ${total_value:.2f}")