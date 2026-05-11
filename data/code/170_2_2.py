class Inventory:
    def __init__(self):
        self.items = {}
    def add_item(self, item_id, item_name, quantity):
        if item_id in self.items:
            raise ValueError(f"Item ID {item_id} already exists in the inventory.")
        self.items[item_id] = {"name": item_name, "quantity": quantity}
if __name__ == '__main__':
    my_inventory = Inventory()
    try:
        my_inventory.add_item(101, "Laptop", 5)
        print("Item 101 added successfully.")
        my_inventory.add_item(102, "Mouse", 20)
        print("Item 102 added successfully.")
        my_inventory.add_item(101, "Monitor", 3)
        print("Item 101 added successfully.")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nCurrent Inventory:")
    for item_id, details in my_inventory.items.items():
        print(f"ID: {item_id}, Name: {details['name']}, Quantity: {details['quantity']}")