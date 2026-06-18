import json
def build_item_list(items_data):
    processed_items = []
    for index, data in enumerate(items_data):
        try:
            cleaned_entry = {
                "id": f"item_{index + 1}",
                **data
            }
            if not isinstance(cleaned_entry.get("name"), str) or len(cleaned_entry["name"]) == 0:
                raise ValueError(f"Invalid name for item at index {index}")
            processed_items.append({
                "id": cleaned_entry["id"],
                "name": cleaned_entry["name"].strip(),
                "price": float(data.get("price", 0.0)),
                "in_stock": data.get("in_stock", True)
            })
        except (ValueError, TypeError):
            continue
    return processed_items
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Laptop", "price": 999.50, "in_stock": True},
        {"id": 2, "name": "Mouse", "price": 25.00, "in_stock": False},
        {"id": 3, "name": "", "price": 10.00, "in_stock": True}
    ]
    result = build_item_list(sample_data)
    output_json = json.dumps(result, indent=2)
    print(output_json)