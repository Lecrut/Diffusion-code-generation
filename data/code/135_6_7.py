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
    sample_json1 = {'b': 2, 'a': 1}
    sample_json2 = {'a': 1, 'b': 2}
    print(are_json_equivalent(sample_json1, sample_json2))
    sample_json3 = {'c': [3, 2], 'a': 1}
    sample_json4 = {'a': 1, 'c': [2, 3]}
    print(are_json_equivalent(sample_json3, sample_json4))
    sample_json5 = {'d': {'e': 4}, 'a': 1}
    sample_json6 = {'a': 1, 'd': {'f': 4}}
    print(are_json_equivalent(sample_json5, sample_json6))