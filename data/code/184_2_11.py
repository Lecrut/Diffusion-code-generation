import json

def find_keyword_in_json(json_data, target_keyword):
    if isinstance(json_data, dict):
        return any((find_keyword_in_json(value, target_keyword) for value in json_data.values()))
    elif isinstance(json_data, list):
        return any((find_keyword_in_json(item, target_keyword) for item in json_data))
    elif isinstance(json_data, str):
        return target_keyword in json_data
    return False
if __name__ == '__main__':
    sample_json = '\n    {\n        "name": "John",\n        "age": 30,\n        "address": {\n            "street": "123 Elm St",\n            "city": "Somewhere"\n        },\n        "hobbies": ["reading", "traveling"]\n    }\n    '
    target_keyword = 'traveling'
    result = find_keyword_in_json(json.loads(sample_json), target_keyword)
    print(result)