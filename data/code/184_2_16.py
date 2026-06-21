import json

def find_keyword_in_json(json_data, target_keyword):
    if isinstance(json_data, dict):
        return any(find_keyword_in_json(value, target_keyword) for value in json_data.values())
    elif isinstance(json_data, list):
        return any(find_keyword_in_json(item, target_keyword) for item in json_data)
    elif isinstance(json_data, str):
        return target_keyword in json_data
    return False

if __name__ == '__main__':
    sample_json = '''
    {
        "key1": "value1",
        "key2": {
            "subkey1": "target_keyword",
            "subkey2": ["list_item", {"nested_key": "target_keyword"}]
        },
        "key3": "value3"
    }
    '''
    target_word = "target_keyword"
    json_data = json.loads(sample_json)
    result = find_keyword_in_json(json_data, target_word)
    print(result)