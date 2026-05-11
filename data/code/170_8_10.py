class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_id, quantity):
        if not isinstance(item_id, int) or item_id <= 0 or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid item ID or quantity provided.")
        if item_id in self.items:
            self.items[item_id] += quantity
        else:
            self.items[item_id] = quantity
    def get_item(self, item_id):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Invalid item ID provided.")
        if item_id in self.items:
            return self.items[item_id]
        else:
            raise KeyError(f"Item ID {item_id} not found.")
if __name__ == '__main__':
    inventory = Inventory()
    print("--- Testing Add Item ---")
    try:
        inventory.add_item(101, 5)
        inventory.add_item(102, 10)
        print("Items added successfully.")
    except ValueError as e:
        print(f"Error during addition: {e}")
    print("\n--- Testing Invalid Add Item (Negative Quantity) ---")
    try:
        inventory.add_item(103, -2)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    print("\n--- Testing Invalid Add Item (Invalid ID Type) ---")
    try:
        inventory.add_item("abc", 5)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    print("\n--- Testing Get Item (Valid ID) ---")
    try:
        quantity = inventory.get_item(101)
        print(f"Quantity for item 101: {quantity}")
    except (ValueError, KeyError) as e:
        print(f"Error during retrieval: {e}")
    print("\n--- Testing Get Item (Non-existent ID) ---")
    try:
        quantity = inventory.get_item(999)
        print(f"Quantity for item 999: {quantity}")
    except (ValueError, KeyError) as e:
        print(f"Caught expected error: {e}")
    print("\n--- Testing Get Item (Invalid ID Type) ---")
    try:
        inventory.get_item("xyz")
    except (ValueError, KeyError) as e:
        print(f"Caught expected error: {e}")