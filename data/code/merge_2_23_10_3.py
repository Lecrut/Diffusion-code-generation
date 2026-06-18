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
        ("banana", 3.0),
        ("cherry", -1),
        (None, 2)
    ]
    for item_name, raw_quantity in sample_items:
        if not isinstance(item_name, str):
            print(f"Skipping invalid item name type.")
            continue
        validated_qty = validate_quantity(raw_quantity)
        if validated_qty is None:
            print("Validation failed. Skipping this entry.")
            continue
        inventory[item_name] = validated_qty
    output_data = {item: qty for item, qty in inventory.items()}
    with open('inventory.json', 'w') as f:
        json.dump(output_data, f)
if __name__ == '__main__':
    main()