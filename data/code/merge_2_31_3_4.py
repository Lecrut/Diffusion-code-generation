import json
def filter_records(data: list[dict], key: str, value) -> list[dict]:
    filtered = []
    for record in data:
        if isinstance(record.get(key), type(value)) and record[key] == value:
            filtered.append(record)
    return filtered
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 30}
    ]
    key_to_filter = "age"
    value_to_match = 30
    result = filter_records(sample_data, key_to_filter, value_to_match)
    print(json.dumps(result))