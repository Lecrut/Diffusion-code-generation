import json
def validate_item(item: dict) -> bool:
    required_fields = ["id", "name", "price"]
    return all(field in item for field in required_fields) and isinstance(item.get("price"), (int, float))
if __name__ == '__main__':
    sample_data = [
        {"id": 101, "name": "Laptop", "price": 999.5},
        {"id": 102, "name": "Mouse", "price": 25},
        {"id": 103, "missing_field": True}
    ]
    validated_items = [item for item in sample_data if validate_item(item)]
    output_json = json.dumps(validated_items)