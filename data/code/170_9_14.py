class InventoryCalculator:
    def __init__(self):
        self.items = {}

    @staticmethod
    def calculate_total_value(items):
        return sum(item['quantity'] * item['price'] for item in items.values())

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            self.items[item_id]['quantity'] += quantity
            self.items[item_id]['price'] = price
        else:
            self.items[item_id] = {'name': name, 'quantity': quantity, 'price': price}

    def display_inventory(self):
        print("--- Inventory Report ---")
        if not self.items:
            print("Inventory is empty.")
        else:
            for item_id, details in self.items.items():
                print(f"Item ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: ${details['price']}")

if __name__ == '__main__':
    inventory = InventoryCalculator()
    inventory.add_item('001', 'Laptop', 3, 999)
    inventory.add_item('002', 'Mouse', 5, 20)
    print(f"Total Value: ${InventoryCalculator.calculate_total_value(inventory.items)}")
    inventory.display_inventory()