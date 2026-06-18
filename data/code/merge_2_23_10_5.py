import json
def validate_quantity(value):
    try:
        quantity = int(float(str(value).strip()))
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")
        return quantity
    except (ValueError, TypeError) as e:
        print(f"Invalid input for quantity: {e}")
        return None
def main():
    inventory = {}
    sample_items = [
        ("apple", 5),
        ("banana", 3),
        ("orange", 0),
        ("grape", -2)
    ]
    print("Processing hard-coded samples...")
    for item_name, quantity in sample_items:
        if not isinstance(item_name, str):
            raise TypeError(f"Item name must be a string. Got {type(item_name)}.")
        validated_qty = validate_quantity(quantity)
        if validated_qty is None:
            continue
        inventory[item_name] = validated_qty
    print("Final Inventory:")
    for item in sorted(inventory.keys()):
        print(f"{item}: {inventory[item]}")
if __name__ == '__main__':
    main()