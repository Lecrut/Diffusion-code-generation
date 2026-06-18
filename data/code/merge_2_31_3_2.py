import json
def filter_records(data: list[dict], key: str, value) -> list[dict]:
    return [record for record in data if record.get(key) == value]
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 30}
    ]
    filtered = filter_records(sample_data, "age", 30)
    print(json.dumps(filtered))