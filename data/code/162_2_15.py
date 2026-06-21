import json

def construct_json_structure():
    data = {
        "name": "John Doe",
        "age": 30,
        "is_employee": True,
        "skills": ["Python", "JavaScript", "SQL"]
    }
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    print(construct_json_structure())