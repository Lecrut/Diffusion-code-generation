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
            print("{:<10} {:<20} {:<10} {:<10.2f}".format(
                item_id, data['name'], data['quantity'], data['price']
            ))
        print("------------------------")
def main():
    inventory = Inventory()
    inventory.add_item(101, "Laptop", 10, 1200.50)
    inventory.add_item(102, "Mouse", 50, 25.99)
    inventory.add_item(103, "Keyboard", 30, 75.00)
    inventory.add_item(101, "Laptop", 5, 1250.00)
    inventory.add_item(104, "Monitor", 15, 350.75)
    inventory.display_inventory()
if __name__ == '__main__':
    main()