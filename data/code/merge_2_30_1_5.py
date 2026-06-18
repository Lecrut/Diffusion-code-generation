import json
def categorize_records(records):
    categorized = {"names": [], "ages": []}
    for record in records:
        name_key = None
        age_key = None
        if isinstance(record.get("name"), str) and len(str(record["name"])) > 0:
            name_key = True
        if isinstance(record.get("age"), int):
            age_key = True
        if name_key is not None or age_key is not None:
            record_copy = {"id": record.get("id", "unknown")}
            if name_key:
                categorized["names"].append({"name": str(record["name"]), "record_id": record_copy})
            if age_key:
                categorized["ages"].append({"age": int(record["age"]), "record_id": record_copy})
    return categorized
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "", "age": None},
        {"id": 4, "name": "Charlie", "age": 35}
    ]
    result = categorize_records(sample_data)
    print(json.dumps(result))