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
        print(f"{'ID':<10} {'Name':<20} {'Quantity':<10} {'Price':<10}")
        print("-" * 44)
        for item_id, data in self.items.items():
            print(f"{item_id:<10} {data['name']:<20} {data['quantity']:<10} {data['price']:<10.2f}")
        print("------------------------")
if __name__ == '__main__':
    inventory_system = Inventory()
    inventory_system.add_item(101, "Laptop", 5, 1200.50)
    inventory_system.add_item(102, "Mouse", 20, 25.99)
    inventory_system.add_item(103, "Keyboard", 15, 75.00)
    inventory_system.add_item(101, "Laptop", 3, 1200.50)
    inventory_system.add_item(104, "Monitor", 8, 350.75)
    inventory_system.display_inventory()