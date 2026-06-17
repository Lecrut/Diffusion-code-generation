import json
def filter_records(records: list[dict], filters: dict) -> list[dict]:
    return [record for record in records if all(record.get(key) == value for key, value in filters.items())]
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 30}
    ]
    filter_criteria = {"age": 30}
    filtered_records = filter_records(sample_data, filter_criteria)
    print(json.dumps(filtered_records))