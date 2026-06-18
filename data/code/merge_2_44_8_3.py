import json
def flatten_structure(data):
    flattened = []
    def recursive_flatten(obj, prefix=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_key = f"{prefix}_{key}" if prefix else key
                if isinstance(value, (dict, list)):
                    recursive_flatten(value, new_key)
                elif not isinstance(value, str):
                    flattened.append({new_key: value})
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                new_prefix = f"{prefix}_list_{idx}" if prefix else f"item_{idx}"
                recursive_flatten(item, new_prefix)
    def process_list(lst, index=0):
        result = []
        for i, item in enumerate(lst):
            if isinstance(item, (dict, list)):
                processed_item = {}
                recursive_flatten(item, f"item_{i}")
                result.extend(processed_item)
            else:
                result.append({"value": item})
        return result
    if isinstance(data, list):
        return process_list(data)
    recursive_flatten(data)
    return flattened
if __name__ == '__main__':
    sample_data = {
        "user_id": 101,
        "profile": {
            "age": 30,
            "hobbies": ["reading", "coding"],
            "address": {
                "city": "New York",
                "zipcode": "10001"
            }
        },
        "orders": [
            {"order_id": 500, "total": 99.9},
            {"order_id": 501, "items": ["apple", "banana"]}
        ]
    }
    flattened_records = flatten_structure(sample_data)
    print(json.dumps(flattened_records))