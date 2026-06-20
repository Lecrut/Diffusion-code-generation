import json

def normalize_key(key):
    if isinstance(key, str):
        return key.lower()
    elif isinstance(key, int) or isinstance(key, float):
        return str(key)
    else:
        raise ValueError("Invalid key type")

def normalize_value(value):
    if isinstance(value, dict):
        return {normalize_key(k): normalize_value(v) for k, v in sorted(value.items())}
    elif isinstance(value, list):
        return [normalize_value(item) for item in value]
    elif isinstance(value, str):
        return value.lower()
    elif isinstance(value, int) or isinstance(value, float):
        return value
    else:
        raise ValueError("Invalid value type")

def are_json_equivalent(json1, json2):
    try:
        normalized_json1 = normalize_value(json.loads(json1))
        normalized_json2 = normalize_value(json.loads(json2))
        return normalized_json1 == normalized_json2
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Invalid JSON input: {e}")
        return False

if __name__ == '__main__':
    sample_json1 = '{"b": 2, "a": 1}'
    sample_json2 = '{"a": 1, "b": 2}'
    print(are_json_equivalent(sample_json1, sample_json2))

    sample_json3 = '{"c": [3], "b": 2, "a": 1}'
    sample_json4 = '{"a": 1, "b": 2, "c": [3]}'
    print(are_json_equivalent(sample_json3, sample_json4))