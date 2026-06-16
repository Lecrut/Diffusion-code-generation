import re
def validate_item_name(name):
    if not name:
        raise ValueError("Item name cannot be empty.")
    pattern = r'^[a-zA-Z0-9\s\-]+$'
    if not re.match(pattern, name.strip()):
        raise ValueError(f"Invalid item name '{name}'. Only alphanumeric characters and spaces/hyphens are allowed.")
def validate_quantity(value):
    try:
        quantity = int(float(value))                                           
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        return quantity
    except (ValueError, TypeError) as e:
        raise ValueError(f"Invalid quantity '{value}'. Must be a non-negative integer.") from e
def add_item(items_dict, name, quantity):
    validate_item_name(name)
    validate_quantity(quantity)
    if name in items_dict:
        items_dict[name] += quantity
    else:
        items_dict[name] = quantity
    return True
if __name__ == '__main__':
    inventory = {}
    try:
        add_item(inventory, "Apple", 5)
    except ValueError as e:
        print(f"Error adding 'Apple': {e}")
    try:
        add_item(inventory, "Banana", 3)
    except ValueError as e:
        print(f"Error adding 'Banana': {e}")
    try:
        add_item(inventory, "@Symbol#123", 4)
    except ValueError as e:
        print(f"Expected error for invalid item name: {e}")
    try:
        add_item(inventory, "Orange", -5)
    except ValueError as e:
        print(f"Error adding 'Orange': {e}")
    if inventory:
        for item in sorted(inventory.keys()):
            print(f"{item}: {inventory[item]}")
    else:
        print("Inventory is empty.")