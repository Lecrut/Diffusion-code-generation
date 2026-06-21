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
        for item_id, item in self.items.items():
            print(f"Item ID: {item_id}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")

if __name__ == '__main__':
    inv = Inventory()
    inv.add_item('001', 'Laptop', 10, 999.99)
    inv.add_item('002', 'Mouse', 50, 19.99)
    inv.display_inventory()