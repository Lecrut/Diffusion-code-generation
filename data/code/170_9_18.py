class Inventory:
    def __init__(self):
        self.items = {}

    @staticmethod
    def _update_item(items, item_id, quantity, price):
        if item_id in items:
            items[item_id]['quantity'] += quantity
            items[item_id]['price'] = price
        else:
            items[item_id] = {
                'name': item_id,
                'quantity': quantity,
                'price': price
            }

    def add_item(self, item_id, name, quantity, price):
        Inventory._update_item(self.items, item_id, quantity, price)

    def display_inventory(self):
        print("--- Inventory Report ---")
        if not self.items:
            print("Inventory is empty.")
        else:
            for item_id, details in self.items.items():
                print(f"Item ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}")

if __name__ == '__main__':
    inv = Inventory()
    inv.add_item('1', 'Laptop', 5, 1000)
    inv.add_item('2', 'Mouse', 20, 30)
    inv.display_inventory()