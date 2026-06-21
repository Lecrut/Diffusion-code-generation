import json

def validate_name_value_pairs(name_value_pairs):
    if not isinstance(name_value_pairs, dict) or not all(isinstance(k, str) and isinstance(v, (int, str)) for k, v in name_value_pairs.items()):
        raise ValueError("Invalid name-value pairs format")

def construct_json_structure(name_value_pairs):
    validate_name_value_pairs(name_value_pairs)
    return json.dumps(name_value_pairs, indent=4)

if __name__ == '__main__':
    sample_values = {
        "user": "Alice",
        "age": 30,
        "active": True
    }
    print(construct_json_structure(sample_values))