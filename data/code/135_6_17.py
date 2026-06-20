import json

def normalize_key(key):
    return str(key).lower()

def normalize_value(value):
    if isinstance(value, dict):
        return {normalize_key(k): normalize_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [normalize_value(item) for item in value]
    else:
        return value

def are_json_equivalent(json1, json2):
    normalized_json1 = normalize_value(json.loads(json1))
    normalized_json2 = normalize_value(json.loads(json2))
    return normalized_json1 == normalized_json2

if __name__ == '__main__':
    sample_json1 = '{"b": 2, "a": 1}'
    sample_json2 = '{"a": 1, "b": 2}'
    print(are_json_equivalent(sample_json1, sample_json2))