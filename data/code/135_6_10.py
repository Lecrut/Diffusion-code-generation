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

def are_equivalent_jsons(json1, json2):
    return canonicalize_json(json1) == canonicalize_json(json2)

if __name__ == '__main__':
    sample_json1 = {
        "Name": "John",
        "Age": 30,
        "Address": {
            "Street": "123 Elm St",
            "City": "Somewhere"
        }
    }

    sample_json2 = {
        "address": {
            "city": "somewhere",
            "street": "123 elm st"
        },
        "age": 30,
        "name": "john"
    }

    print(are_equivalent_jsons(sample_json1, sample_json2))