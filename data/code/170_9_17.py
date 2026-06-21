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

        for item_id, details in self.items.items():
            print(f"Item ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}")

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('001', 'Laptop', 5, 999.99)
    inventory.add_item('002', 'Mouse', 30, 19.99)
    inventory.display_inventory()