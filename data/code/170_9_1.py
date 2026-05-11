import json
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
    def display_inventory(self):
        print("--- Inventory Report ---")
        if not self.items:
            print("Inventory is empty.")
            return
        print("{:<10} {:<20} {:<10} {:<10}".format("ID", "Name", "Quantity", "Price"))
        print("-" * 42)
        for item_id, data in self.items.items():
            print("{:<10} {:<20} {:<10} ${:<9.2f}".format(
                item_id, data['name'], data['quantity'], data['price']
            ))
        print("------------------------")
    def save_to_file(self, filename="inventory.json"):
        with open(filename, 'w') as f:
            json.dump(self.items, f, indent=4)
def initialize_inventory():
    inv = Inventory()
    inv.add_item(101, "Laptop", 15, 1200.50)
    inv.add_item(102, "Mouse", 50, 25.99)
    inv.add_item(103, "Keyboard", 30, 75.00)
    inv.add_item(104, "Monitor", 10, 350.75)
    inv.display_inventory()
    inv.save_to_file()
if __name__ == '__main__':
    initialize_inventory()