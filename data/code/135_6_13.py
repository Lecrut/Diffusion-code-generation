import json

def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError:
        return False

def normalize_json(obj):
    if isinstance(obj, dict):
        return {normalize_json(k): normalize_json(v) for k, v in sorted(obj.items())}
    elif isinstance(obj, list):
        return [normalize_json(item) for item in obj]
    else:
        return obj

def are_json_equivalent(json1, json2):
    if not is_valid_json(json1) or not is_valid_json(json2):
        raise ValueError("Both inputs must be valid JSON strings.")
    
    normalized_json1 = normalize_json(json.loads(json1))
    normalized_json2 = normalize_json(json.loads(json2))
    
    return normalized_json1 == normalized_json2

if __name__ == '__main__':
    sample_json1 = '{"b": 2, "a": 1}'
    sample_json2 = '{"a": 1, "b": 2}'
    print(are_json_equivalent(sample_json1, sample_json2))