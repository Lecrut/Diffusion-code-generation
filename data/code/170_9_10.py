class InventoryCalculator:
    def __init__(self):
        self.items = {}

    @staticmethod
    def calculate_total_cost(items):
        return sum(item['quantity'] * item['price'] for item in items)

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.items:
            self.items[item_id]['quantity'] += quantity
            self.items[item_id]['price'] = price
        else:
            self.items[item_id] = {'name': name, 'quantity': quantity, 'price': price}

    def display_inventory(self):
        print("--- Inventory Report ---")
        for item_id, details in self.items.items():
            print(f"Item ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}, Price: {details['price']}")
        total_cost = self.calculate_total_cost(self.items.values())
        print(f"Total Inventory Cost: {total_cost}")

if __name__ == '__main__':
    inventory = InventoryCalculator()
    inventory.add_item('001', 'Laptop', 5, 999)
    inventory.add_item('002', 'Mouse', 20, 10)
    inventory.display_inventory()