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

def canonical_form(obj):
    return json.dumps(normalize_value(obj), sort_keys=True)

def are_equivalent_jsons(json1, json2):
    return canonical_form(json1) == canonical_form(json2)

if __name__ == '__main__':
    sample_json1 = {
        "Name": "Alice",
        "Age": 30,
        "Children": [
            {"Name": "Bob", "Age": 10},
            {"Name": "Charlie", "Age": 5}
        ]
    }
    
    sample_json2 = {
        "age": 30,
        "name": "alice",
        "children": [
            {"age": 10, "name": "bob"},
            {"age": 5, "name": "charlie"}
        ]
    }

    print(are_equivalent_jsons(sample_json1, sample_json2))