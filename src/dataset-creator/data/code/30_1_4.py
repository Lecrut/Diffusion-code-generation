import json
def categorize_records(records):
    categorized = {"names": [], "ages": []}
    for record in records:
        if isinstance(record.get("type"), str) and record["type"] == "name" and isinstance(record.get("value"), str):
            categorized["names"].append(record["value"])
        elif isinstance(record.get("type"), str) and record["type"] == "age" and isinstance(record.get("value"), int):
            categorized["ages"].append(record["value"])
    return categorized
if __name__ == '__main__':
    sample_data = [
        {"type": "name", "value": "Alice"},
        {"type": "age", "value": 30},
        {"type": "name", "value": "Bob"},
        {"type": "age", "value": 25}
    ]
    result = categorize_records(sample_data)
    print(json.dumps(result, indent=4))