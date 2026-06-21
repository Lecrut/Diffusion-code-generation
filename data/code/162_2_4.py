import json

def construct_json_structure():
    name_value_pairs = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return json.dumps(name_value_pairs, indent=4)

if __name__ == '__main__':
    print(construct_json_structure())