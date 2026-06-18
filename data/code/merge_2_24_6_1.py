import json
def validate_and_populate(data):
    required_fields = ["id", "name", "price"]
    if not isinstance(data, dict) or data == {}:
        return []
    validated_items = []
    for item in data:
        if not isinstance(item, dict):
            continue
        missing_fields = [field for field in required_fields if field not in item]
        if missing_fields:
            print(f"Warning: Item {item.get('id', 'unknown')} is missing fields: {missing_fields}")
            continue
        validated_items.append(item)
    return validated_items
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Laptop", "price": 999.99},
        {"id": 2, "name": "Mouse"},
        {"id": 3, "name": "Keyboard", "missing_field": True}
    ]
    try:
        json_input = json.dumps(sample_data)
        parsed_json = json.loads(json_input)
        result_items = validate_and_populate(parsed_json)
        output_list = [{"status": "valid"} for _ in range(len(result_items))]
        print(f"Validated items count: {len(output_list)}")
    except Exception as e:
        print(f"Error processing data: {e}")