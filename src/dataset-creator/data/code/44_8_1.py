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
        cleaned_record = {k: v if isinstance(v, str) else str(v) for k, v in record.items()}
        transformed.append(cleaned_record)
    return transformed
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 123, "details": {"name": "Alice", "age": 30}},
        "posts": [
            {"title": "Post One", "content": "Hello World"},
            {"title": "Post Two", "tags": ["python", "code"]}
        ]
    }
    flattened = flatten_structure(sample_data)
    transformed_list = transform_records(flattened)
    print(json.dumps(transformed_list, indent=2))