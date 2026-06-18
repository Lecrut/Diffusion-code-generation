import json
def validate_quantity(value):
    try:
        quantity = int(float(str(value).strip()))
        if quantity < 0:
            raise ValueError("Quantity must be non-negative")
        return quantity
    except (ValueError, TypeError) as e:
        print(f"Invalid input for quantity: {e}")
        return None
def main():
    inventory = {}
    sample_items = [
        {"name": "Apple", "quantity": 10},
        {"name": "Banana", "quantity": 5},
        {"name": "Orange", "quantity": -3}
    ]
    for item in sample_items:
        name = str(item["name"]).strip()
        if not name:
            print("Item name cannot be empty.")
            continue
        quantity_result = validate_quantity(item.get("quantity"))
        if quantity_result is None:
            inventory[name] = 0
        else:
            inventory[name] = quantity_result
    output_data = {"inventory": json.dumps(inventory, indent=4)}
    with open('final_inventory.json', 'w') as f:
        json.dump(output_data, f)
if __name__ == '__main__':
    main()