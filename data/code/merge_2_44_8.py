import json
def flatten_structure(data):
    flattened = []
    def recursive_flatten(obj, prefix=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_prefix = f"{prefix}.{key}" if prefix else str(key)
                if isinstance(value, (dict, list)):
                    recursive_flatten(value, new_prefix)
                elif not isinstance(value, str):
                    flattened.append({new_prefix: value})
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                new_prefix = f"{prefix}[{idx}]" if prefix else str(idx)
                recursive_flatten(item, new_prefix)
    recursive_flatten(data)
    return flattened
def transform_records(records):
    transformed = []
    for record in records:
        try:
            parsed_record = json.loads(json.dumps(record))                             
            if isinstance(parsed_record, dict) and 'id' not in parsed_record:
                parsed_record['id'] = len(transformed) + 1
            transformed.append(parsed_record)
        except (json.JSONDecodeError, TypeError):
            continue
    return transformed
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 101, "details": {"name": "Alice", "age": 30}},
        "orders": [
            {"order_id": 5001, "items": [{"sku": "A", "qty": 2}, {"sku": "B", "qty": 1}]},
            {"order_id": 5002, "items": []}
        ],
        "metadata": {
            "created_at": "2023-01-01",
            "active": True
        }
    }
    flat_records = flatten_structure(sample_data)
    final_output = transform_records(flat_records)
    print(json.dumps(final_output, indent=4))