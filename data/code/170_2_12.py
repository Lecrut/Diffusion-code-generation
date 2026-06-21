from collections import defaultdict

class InventoryManager:
    def __init__(self):
        self.items = defaultdict(int)
    
    def add_items(self, items):
        for item_id, quantity in items.items():
            if not isinstance(item_id, int) or not isinstance(quantity, (int, float)):
                raise ValueError("Invalid input: Item ID must be an integer and quantity must be a number.")
            self.items[item_id] += quantity
    
    def get_total_value(self, price_per_item):
        if not isinstance(price_per_item, dict):
            raise ValueError("Price per item must be a dictionary with item IDs as keys.")
        
        total_value = 0
        for item_id, quantity in self.items.items():
            if item_id not in price_per_item:
                raise KeyError(f"Item ID {item_id} not found in price per item dictionary.")
            total_value += price_per_item[item_id] * quantity
        
        return total_value

if __name__ == '__main__':
    inventory_manager = InventoryManager()
    try:
        inventory_manager.add_items({101: 50, 102: 30})
        print("Items added successfully.")
        inventory_manager.add_items({101: 10})
        print("Items added successfully.")
        
        price_per_item = {101: 1.0, 102: 0.5}
        total_value = inventory_manager.get_total_value(price_per_item)
        print(f"Total Inventory Value: ${total_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")