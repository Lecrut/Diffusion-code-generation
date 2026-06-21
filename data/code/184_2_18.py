import json

def find_keyword(json_payload, target_keyword):
    if isinstance(json_payload, dict):
        for key, value in json_payload.items():
            if key == target_keyword:
                return True
            if find_keyword(value, target_keyword):
                return True
    elif isinstance(json_payload, list):
        for item in json_payload:
            if find_keyword(item, target_keyword):
                return True
    return False
if __name__ == '__main__':
    sample_json = '\n    {\n        "root": {\n            "level1": {\n                "level2": ["value1", "value2", "target_keyword"]\n            },\n            "other_key": "other_value"\n        }\n    }\n    '
    target_word = 'target_keyword'
    json_payload = json.loads(sample_json)
    result = find_keyword(json_payload, target_word)
    print(result)