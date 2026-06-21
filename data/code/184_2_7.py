import json

def find_keyword_in_json(payload, keyword):
    if isinstance(payload, dict):
        for key, value in payload.items():
            if key == keyword:
                return True
            if find_keyword_in_json(value, keyword):
                return True
    elif isinstance(payload, list):
        for item in payload:
            if find_keyword_in_json(item, keyword):
                return True
    return False
if __name__ == '__main__':
    sample_json = '\n    {\n        "name": "John",\n        "age": 30,\n        "children": [\n            {\n                "name": "Jane",\n                "age": 10\n            },\n            {\n                "name": "Doe",\n                "age": 5\n            }\n        ],\n        "address": {\n            "street": "123 Main St",\n            "city": "Anytown"\n        }\n    }\n    '
    sample_keyword = 'Jane'
    json_payload = json.loads(sample_json)
    result = find_keyword_in_json(json_payload, sample_keyword)
    print(result)