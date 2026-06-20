import json

def normalize_json(obj):
    if isinstance(obj, dict):
        return {normalize_json(k): normalize_json(v) for k, v in sorted(obj.items())}
    elif isinstance(obj, list):
        return [normalize_json(item) for item in obj]
    else:
        return obj

def are_json_equivalent(json1, json2):
    return normalize_json(json1) == normalize_json(json2)

if __name__ == '__main__':
    sample_json1 = {
        "b": 2,
        "a": 1,
        "c": {"d": 3}
    }
    sample_json2 = {
        "a": 1,
        "b": 2,
        "c": {"d": 3}
    }
    print(are_json_equivalent(sample_json1, sample_json2))