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
        cleaned_record = {k: v if isinstance(v, str) else f"<{type(v).__name__}>" for k, v in record.items()}
        transformed.append(cleaned_record)
    return transformed
if __name__ == '__main__':
    sample_data = [
        {"id": 1, "details": {"nested_key": "value", "items": ["a", "b"]}},
        {"id": 2, "active": True},
        {"id": 3, "metadata": {}}
    ]
    flat_records = flatten_structure(sample_data)
    final_output = transform_records(flat_records)
    print(json.dumps(final_output))