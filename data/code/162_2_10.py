import json

def construct_json_structure():
    name_value_pairs = {
        "name": "Alice Smith",
        "age": 28,
        "is_student": True,
        "major": "Computer Science"
    }
    return json.dumps(name_value_pairs, indent=4)

if __name__ == '__main__':
    print(construct_json_structure())