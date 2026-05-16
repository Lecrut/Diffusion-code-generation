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
        my_inventory.add_item(101, "Apple", 50)
        my_inventory.add_item(102, "Banana", 120)
        my_inventory.add_item(101, "Apple", 10)
    except ValueError as e:
        print(f"Error: {e}")
    print(my_inventory.items)