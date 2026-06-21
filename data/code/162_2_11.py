import json

def construct_json_structure():
    name_value_pairs = {
        "name": "Jane Doe",
        "age": 25,
        "is_employee": False,
        "skills": ["Java", "C++"]
    }
    return json.dumps(name_value_pairs, indent=4)

if __name__ == '__main__':
    print(construct_json_structure())