import json
def transform_csv_to_json(csv_data: list[dict]) -> str:
    if not csv_data:
        return "[]"
    keys = next(iter(csv_data)).keys()
    sorted_keys = sorted(keys, key=lambda k: str(k).lower())
    json_list = []
    for item in csv_data:
        ordered_item = {k: item[k] for k in sorted_keys}
        json_list.append(ordered_item)
    return json.dumps(json_list, ensure_ascii=False, indent=2)
def generate_sample_csv() -> list[dict]:
    return [
        {"id": 101, "name": "Alice", "score": 95.5},
        {"id": 102, "name": "Bob", "score": 87.3},
        {"id": 103, "name": "Charlie", "score": 92.1}
    ]
if __name__ == '__main__':
    raw_data = generate_sample_csv()
    json_output = transform_csv_to_json(raw_data)
    print(json_output)