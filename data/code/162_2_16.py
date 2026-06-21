import json

def construct_json_structure():
    data = {
        "name": "John Doe",
        "age": 30,
        "is_employee": True,
        "skills": ["Python", "JavaScript"]
    }
    return data

if __name__ == '__main__':
    result = construct_json_structure()
    print(json.dumps(result, indent=4))