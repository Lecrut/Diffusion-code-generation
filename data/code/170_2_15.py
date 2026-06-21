from collections import defaultdict

ITEM_PRICE = {
    "Apple": 0.50,
    "Banana": 0.30,
    "Laptop": 1200.00,
    "Mouse": 25.00,
    "Monitor": 75.00
}

class Inventory:
    def __init__(self):
        self.items = defaultdict(int)

    def add_items(self, item_id, item_name, quantity):
        if item_id in self.items:
            raise ValueError(f"Item ID {item_id} already exists in the inventory.")
        self.items[item_id] = {"name": item_name, "quantity": quantity}

    def calculate_total_value(self):
        return sum(quantity * ITEM_PRICE[name] for name, quantity in self.items.values())

if __name__ == '__main__':
    my_inventory = Inventory()
    try:
        my_inventory.add_items(101, "Apple", 50)
        my_inventory.add_items(102, "Banana", 30)
        my_inventory.add_items(103, "Laptop", 5)
    except ValueError as e:
        print(f"Error: {e}")
    print("Total Inventory Value:", my_inventory.calculate_total_value())