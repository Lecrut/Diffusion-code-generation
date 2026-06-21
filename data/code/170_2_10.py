from collections import defaultdict

class Inventory:
    def __init__(self):
        self.items = defaultdict(dict)

    def add_item(self, item_id, item_name, quantity):
        if not isinstance(item_id, int) or item_id < 1:
            raise ValueError("Item ID must be a positive integer.")
        if 'name' in self.items[item_id]:
            raise ValueError(f"Item ID {item_id} already exists in the inventory.")
        self.items[item_id]['name'] = item_name
        self.items[item_id]['quantity'] = quantity

    def add_batch_items(self, batch):
        for item_id, item_info in batch:
            try:
                self.add_item(item_id, item_info['name'], item_info['quantity'])
            except ValueError as e:
                print(f"Error adding item {item_id}: {e}")

    def calculate_total_value(self, price_per_item):
        total_value = 0
        for item_id, item in self.items.items():
            total_value += item['quantity'] * price_per_item[item_id]
        return total_value

if __name__ == '__main__':
    my_inventory = Inventory()
    batch_items = [
        (101, {"name": "Apple", "quantity": 50}),
        (102, {"name": "Banana", "quantity": 30})
    ]
    price_per_item = {
        101: 0.5,
        102: 0.2
    }
    try:
        my_inventory.add_batch_items(batch_items)
        print("Batch items added successfully.")
        total_value = my_inventory.calculate_total_value(price_per_item)
        print(f"Total inventory value: ${total_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")