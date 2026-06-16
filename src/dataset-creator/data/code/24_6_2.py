import json
def validate_item(item: dict) -> bool:
    required_fields = ["id", "name", "price"]
    for field in required_fields:
        if field not in item:
            return False
    try:
        float(item["price"])
    except (ValueError, TypeError):
        return False
    return True
def populate_item_list(json_data: str) -> list:
    parsed = json.loads(json_data)
    items = []
    for entry in parsed.get("items", []):
        if validate_item(entry):
            items.append({"id": entry["id"], "name": entry["name"], "price": float(entry["price"])})
    return items
if __name__ == '__main__':
    sample_json = '{"items": [{"id": 1, "name": "Apple", "price": 0.5}, {"id": 2, "missing_field": true}]}'
    result_list = populate_item_list(sample_json)
    print(result_list)