import json
def categorize_records(records):
    categorized = {"names": [], "ages": []}
    for record in records:
        if isinstance(record.get("name"), str) and len(str(record["name"])) > 0:
            categorized["names"].append(record["name"])
        age_value = record.get("age")
        try:
            int_age = int(age_value)
            if int_age >= 0:
                categorized["ages"].append(int_age)
        except (ValueError, TypeError):
            pass
    return categorized
if __name__ == '__main__':
    sample_data = [
        {"id": "1", "name": "Alice", "age": "25"},
        {"id": "2", "name": "Bob", "age": "30"},
        {"id": "3", "name": "", "age": "-5"},
        {"id": "4", "name": "Charlie", "age": 99},
    ]
    result = categorize_records(sample_data)
    print(json.dumps(result, indent=2))