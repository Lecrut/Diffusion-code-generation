import json
def validate_entry(entry):
    errors = []
    if not isinstance(entry, dict):
        return ["Entry must be a dictionary."]
    name_val = entry.get('name')
    if name_val is None:
        errors.append("'name' key is missing.")
    elif not isinstance(name_val, str):
        errors.append(f"'name' value must be a string, got {type(name_val).__name__}.")
    category_val = entry.get('category')
    if category_val is None:
        errors.append("'category' key is missing.")
    elif not isinstance(category_val, str):
        errors.append(f"'category' value must be a string, got {type(category_val).__name__}.")
    price_val = entry.get('price')
    if price_val is None:
        errors.append("'price' key is missing.")
    elif not isinstance(price_val, (int, float)):
        errors.append(f"'price' value must be a number, got {type(price_val).__name__}.")
    quantity_val = entry.get('quantity')
    if quantity_val is None:
        errors.append("'quantity' key is missing.")
    elif not isinstance(quantity_val, int):
        errors.append(f"'quantity' value must be an integer, got {type(quantity_val).__name__}.")
    in_stock_val = entry.get('in_stock')
    if in_stock_val is None:
        errors.append("'in_stock' key is missing.")
    elif not isinstance(in_stock_val, bool):
        errors.append(f"'in_stock' value must be a boolean, got {type(in_stock_val).__name__}.")
    return errors
def organize_data(raw_entries):
    organized = {"objects": []}
    invalid_count = 0
    for idx, entry in enumerate(raw_entries):
        error_messages = validate_entry(entry)
        if not error_messages:
            obj_data = {
                "id": f"obj_{idx}",
                **entry
            }
            organized["objects"].append(obj_data)
        else:
            invalid_count += 1
    return organized, invalid_count
if __name__ == '__main__':
    raw_entries = [
        {"name": "Laptop", "category": "Electronics", "price": 999.50, "quantity": 10, "in_stock": True},
        {"name": "Desk Chair", "category": "Furniture", "price": 250.00, "quantity": 5, "in_stock": False},
        {"name": 123456789, "category": "Invalid Price Type", "price": "not a number", "quantity": 2, "in_stock": True},                                               
        {"name": "Monitor", "category": "Electronics", "price": 300.00, "quantity": -5, "in_stock": False},                                                            
        None,                           
        {},                   
    ]
    try:
        structured_data, error_count = organize_data(raw_entries)
        print("Organized Data Structure:")
        print(json.dumps(structured_data, indent=2))
        print(f"\nValidation Summary:")
        if error_count > 0:
            print(f"Found {error_count} malformed entries.")
        else:
            print("All entries were valid.")
    except Exception as e:
        print(f"An unexpected system error occurred while organizing data: {str(e)}")