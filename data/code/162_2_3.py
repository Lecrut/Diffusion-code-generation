import json

def construct_json_mapping():
    name_value_pairs = {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "courses": ["Math", "Science"]
    }
    
    return json.dumps(name_value_pairs, indent=4)

if __name__ == '__main__':
    print(construct_json_mapping())