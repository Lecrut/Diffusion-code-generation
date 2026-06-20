import json

def normalize_key(key):
    return key.lower()

def normalize_value(value):
    if isinstance(value, dict):
        return {normalize_key(k): normalize_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [normalize_value(item) for item in value]
    else:
        return value

def canonicalize_json(json_obj):
    normalized = normalize_value(json_obj)
    return json.dumps(normalized, sort_keys=True)

def are_json_objects_equivalent(obj1, obj2):
    return canonicalize_json(obj1) == canonicalize_json(obj2)
if __name__ == '__main__':
    sample1 = {'Name': 'John', 'Age': 30, 'Address': {'Street': '123 Main St', 'City': 'Anytown'}}
    sample2 = {'address': {'city': 'Anytown', 'street': '123 Main St'}, 'age': 30, 'name': 'John'}
    print(are_json_objects_equivalent(sample1, sample2))