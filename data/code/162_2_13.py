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
    return data

if __name__ == '__main__':
    json_data = construct_json_structure()
    print(json.dumps(json_data, indent=4))