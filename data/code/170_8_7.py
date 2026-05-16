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
        if item_id in self.items:
            return self.items[item_id]
        else:
            raise KeyError(f"Item ID {item_id} not found in inventory.")
if __name__ == '__main__':
    inventory = Inventory()
    print("--- Testing Add Item ---")
    try:
        inventory.add_item(101, 5)
        inventory.add_item(102, 10)
        print("Successfully added items.")
    except ValueError as e:
        print(f"Error during addition: {e}")
    print("\n--- Testing Invalid Item ID Addition ---")
    try:
        inventory.add_item(-5, 2)
    except ValueError as e:
        print(f"Caught expected error for invalid ID: {e}")
    print("\n--- Testing Retrieval ---")
    try:
        quantity101 = inventory.get_item(101)
        print(f"Quantity for item 101: {quantity101}")
        quantity999 = inventory.get_item(999)
    except KeyError as e:
        print(f"Caught expected error for missing item: {e}")
    print("\n--- Testing Retrieval of Non-existent Item ---")
    try:
        inventory.get_item(999)
    except KeyError as e:
        print(f"Caught expected error for non-existent item: {e}")