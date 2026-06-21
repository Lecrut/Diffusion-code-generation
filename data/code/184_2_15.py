import json

def find_keyword_in_json(payload, keyword):
    if isinstance(payload, dict):
        for key, value in payload.items():
            if key == keyword:
                return True
            elif find_keyword_in_json(value, keyword):
                return True
    elif isinstance(payload, list):
        for item in payload:
            if find_keyword_in_json(item, keyword):
                return True
    return False

if __name__ == '__main__':
    sample_json = '''
    {
        "root": {
            "level1": {
                "level2": ["item1", "item2", {"key": "value"}]
            },
            "another_key": "another_value"
        }
    }
    '''
    keyword_to_find = 'key'
    payload = json.loads(sample_json)
    result = find_keyword_in_json(payload, keyword_to_find)
    print(result)