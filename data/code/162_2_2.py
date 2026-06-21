import json

def construct_json_structure():
    name_value_pairs = {
        "name": "John Doe",
        "age": 30,
        "is_employee": True,
        "skills": ["Python", "JavaScript"]
    }
    return json.dumps(name_value_pairs, indent=4)

if __name__ == '__main__':
    print(construct_json_structure())