import json
def validate_and_populate(data):
    required_fields = ["id", "name", "price"]
    if not isinstance(data, dict) or data.get("type") != "item_list":
        raise ValueError("Invalid input structure: expected a dictionary with 'type' set to 'item_list'.")
    items = []
    for idx, item in enumerate(data["items"], 1):
        missing_fields = [field for field in required_fields if field not in item]
        if missing_fields:
            raise ValueError(f"Item {idx} is invalid. Missing fields: {missing_fields}.")
        items.append({
            "id": int(item["id"]),
            "name": str(item["name"]).strip(),
            "price": float(item["price"])
        })
    return {"status": "success", "count": len(items), "data": items}
if __name__ == '__main__':
    sample_data = {
        "type": "item_list",
        "items": [
            {"id": 101, "name": "Widget A", "price": 9.99},
            {"id": 102, "name": "Gadget B", "price": 45.50}
        ]
    }
    try:
        result = validate_and_populate(sample_data)
        print(json.dumps(result, indent=2))
    except ValueError as e:
        print(f"Validation Error: {e}")