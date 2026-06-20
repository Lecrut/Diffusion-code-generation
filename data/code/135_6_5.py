import json

def normalize(obj):
    if isinstance(obj, dict):
        return {normalize(k): normalize(v) for k, v in sorted(obj.items())}
    elif isinstance(obj, list):
        return [normalize(item) for item in obj]
    else:
        return obj

def are_json_objects_equivalent(json1, json2):
    return normalize(json1) == normalize(json2)

if __name__ == '__main__':
    sample1 = '{"b": 2, "a": 1}'
    sample2 = '{"a": 1, "b": 2}'
    print(are_json_objects_equivalent(sample1, sample2))