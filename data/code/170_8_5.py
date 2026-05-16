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
        inventory.add_item(101, 3)
        print("Items added successfully.")
    except ValueError as e:
        print(f"Error during addition: {e}")
    print("\n--- Testing Get Item ---")
    try:
        item101_quantity = inventory.get_item(101)
        print(f"Quantity for item 101: {item101_quantity}")
        item103_quantity = inventory.get_item(103)
        print(f"Quantity for item 103: {item103_quantity}")
    except (KeyError, ValueError) as e:
        print(f"Error during retrieval: {e}")
    print("\n--- Testing Error Handling (Invalid ID) ---")
    try:
        inventory.get_item(-5)
    except (KeyError, ValueError) as e:
        print(f"Successfully caught error for invalid ID - {e}")
    try:
        inventory.add_item("abc", 10)
    except ValueError as e:
        print(f"Successfully caught error for invalid item ID during addition - {e}")
    try:
        inventory.add_item(104, -5)
    except ValueError as e:
        print(f"Successfully caught error for invalid quantity during addition - {e}")