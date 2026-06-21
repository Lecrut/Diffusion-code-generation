from collections import defaultdict

class Inventory:
    def __init__(self):
        self.items = defaultdict(dict)
    
    def add_item(self, item_id, item_name, quantity):
        if not item_id or not item_name or quantity < 0:
            raise ValueError("Invalid input values")
        if 'name' in self.items[item_id]:
            raise ValueError(f"Item ID {item_id} already exists in the inventory.")
        self.items[item_id]['name'] = item_name
        self.items[item_id]['quantity'] = quantity
    
    def add_items(self, batch):
        for item_id, item_details in batch.items():
            try:
                self.add_item(item_id, item_details['name'], item_details['quantity'])
            except ValueError as e:
                print(f"Error adding item {item_id}: {e}")
    
    def calculate_total_value(self, price_per_item):
        total_value = 0
        for item in self.items.values():
            total_value += item['quantity'] * price_per_item[item['name']]
        return total_value

if __name__ == '__main__':
    my_inventory = Inventory()
    try:
        batch = {
            101: {"name": "Apple", "quantity": 50},
            102: {"name": "Banana", "quantity": 30}
        }
        my_inventory.add_items(batch)
        print("Batch added successfully.")
        price_per_item = {
            "Apple": 1.2,
            "Banana": 0.8
        }
        total_value = my_inventory.calculate_total_value(price_per_item)
        print(f"Total inventory value: ${total_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")