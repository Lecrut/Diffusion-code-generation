import json
def validate_and_populate(data):
    required_fields = ["id", "name", "price"]
    if not isinstance(data, dict) and data:
        raise ValueError("Input must be a dictionary.")
    for field in required_fields:
        if field not in data or (isinstance(data[field], str) and len(str(data[field])) == 0):
            return None
    items = []
    try:
        json_str = json.dumps({"id": int(data["id"]), "name": str(data["name"]).strip(), "price": float(data["price"])})
        parsed_data = json.loads(json_str)
        for item in data.get("items", [parsed_data]):
            if not isinstance(item, dict):
                continue
            missing_fields = []
            for field in required_fields:
                val = item.get(field)
                if val is None or (isinstance(val, str) and len(str(val)) == 0):
                    missing_fields.append(field)
            if not all(f in item for f in required_fields):
                continue
            items.append({
                "id": int(item["id"]),
                "name": str(item["name"]).strip(),
                "price": float(item["price"])
            })
    except (ValueError, TypeError) as e:
        return None
    return {"status": "success", "count": len(items)}
if __name__ == '__main__':
    sample_input = {
        "id": 101,
        "name": "Widget A",
        "price": 29.99,
        "items": [
            {"id": 1, "name": "Test Item", "price": 5.0},
            {"id": 2, "name": "", "price": 3.0}
        ]
    }
    result = validate_and_populate(sample_input)
    if result:
        print(json.dumps(result))
    else:
        print("Validation failed or data is invalid.")