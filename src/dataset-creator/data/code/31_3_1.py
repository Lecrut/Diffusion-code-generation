import json
def filter_records(data: list[dict], key: str, value) -> list[dict]:
    return [record for record in data if record.get(key) == value]
if __name__ == '__main__':
    records = [
        {"id": 1, "name": "Alice", "city": "New York"},
        {"id": 2, "name": "Bob", "city": "Los Angeles"},
        {"id": 3, "name": "Charlie", "city": "Chicago"},
    ]
    filtered = filter_records(records, "city", "New York")
    print(json.dumps(filtered))