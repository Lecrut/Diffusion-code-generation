import json

def construct_json_structure():
    data = {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "courses": ["Math", "Science"],
        "address": {
            "street": "123 Elm St",
            "city": "Somewhere",
            "zip": "12345"
        }
    }
    return json.dumps(data, indent=4)

if __name__ == '__main__':
    print(construct_json_structure())