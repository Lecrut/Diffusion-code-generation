import json

def validate_input(input_dict):
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary")

def construct_json_structure():
    name_value_pairs = {
        "name": "John Doe",
        "age": 30,
        "is_employee": True,
        "skills": ["Python", "JavaScript"]
    }
    validate_input(name_value_pairs)
    return json.dumps(name_value_pairs, indent=4)

if __name__ == '__main__':
    print(construct_json_structure())