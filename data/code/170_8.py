class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_id, quantity):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Invalid item ID provided.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Invalid quantity provided.")
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
    print("\n--- Testing Invalid Item ID Addition ---")
    try:
        inventory.add_item(-5, 2)
    except ValueError as e:
        print(f"Caught expected error for invalid ID (-5): {e}")
    print("\n--- Testing Invalid Quantity Addition ---")
    try:
        inventory.add_item(103, -1)
    except ValueError as e:
        print(f"Caught expected error for invalid quantity (-1): {e}")
    print("\n--- Testing Retrieval ---")
    try:
        quantity = inventory.get_item(101)
        print(f"Quantity for item 101: {quantity}")
    except KeyError as e:
        print(f"Error during retrieval: {e}")
    print("\n--- Testing Invalid Item ID Retrieval ---")
    try:
        inventory.get_item(999)
    except ValueError as e:
        print(f"Caught expected error for invalid ID (999): {e}")
    except KeyError as e:
        print(f"Caught expected error for non-existent item: {e}")