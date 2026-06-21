import json

def find_keyword_in_json(json_data, target_keyword):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == target_keyword:
                return True
            if find_keyword_in_json(value, target_keyword):
                return True
    elif isinstance(json_data, list):
        for item in json_data:
            if find_keyword_in_json(item, target_keyword):
                return True
    return False

if __name__ == '__main__':
    sample_json_data = {
        "name": "John",
        "age": 30,
        "address": {
            "street": "123 Elm St",
            "city": "Somewhere"
        },
        "hobbies": ["reading", "traveling"]
    }
    target_keyword = "traveling"
    print(find_keyword_in_json(sample_json_data, target_keyword))