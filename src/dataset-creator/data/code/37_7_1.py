import json
def aggregate_item_counts(source_a: dict, source_b: list) -> dict:
    aggregated = {}
    for item in source_a.get("items", []):
        key = f"{item['id']}-{item['category']}"
        if key not in aggregated:
            aggregated[key] = 0
        aggregated[key] += item["count"]
    for entry in source_b:
        key = f"{entry['product_id']}-{entry['region']}"
        if key not in aggregated:
            aggregated[key] = 0
        aggregated[key] += entry["quantity"]
    return {"total_items": len(aggregated), "details": list(aggregated.items())}
if __name__ == '__main__':
    source_a_data = {
        "items": [
            {"id": "1", "category": "electronics", "count": 5},
            {"id": "2", "category": "clothing", "count": 3},
            {"id": "1", "category": "electronics", "count": 2}
        ]
    }
    source_b_data = [
        {"product_id": "100", "region": "north", "quantity": 4},
        {"product_id": "100", "region": "south", "quantity": 6},
        {"product_id": "200", "region": "east", "quantity": 8}
    ]
    result = aggregate_item_counts(source_a_data, source_b_data)
    print(json.dumps(result, indent=4))