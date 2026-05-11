class Inventory:
    def __init__(self):
        self.items = {
            "apple": 10,
            "banana": 5,
            "orange": 15
        }
    def update_quantity(self, item_name, new_quantity):
        if item_name in self.items:
            self.items[item_name] = new_quantity
            return True
        else:
            return False
if __name__ == '__main__':
    inventory = Inventory()
    print(f"Initial inventory: {inventory.items}")
    item_to_update = "apple"
    new_quantity = 12
    success = inventory.update_quantity(item_to_update, new_quantity)
    if success:
        print(f"Successfully updated quantity of {item_to_update} to {new_quantity}")
    else:
        print(f"Error: Item {item_to_update} not found.")
    item_to_update = "grape"
    new_quantity = 20
    success = inventory.update_quantity(item_to_update, new_quantity)
    if success:
        print(f"Successfully updated quantity of {item_to_update} to {new_quantity}")
    else:
        print(f"Error: Item {item_to_update} not found.")
    print(f"Final inventory: {inventory.items}")