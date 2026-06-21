import json

def find_keyword_in_json(payload, target_keyword):
    if isinstance(payload, dict):
        for key, value in payload.items():
            if key == target_keyword:
                return True
            if find_keyword_in_json(value, target_keyword):
                return True
    elif isinstance(payload, list):
        for item in payload:
            if find_keyword_in_json(item, target_keyword):
                return True
    return False

if __name__ == '__main__':
    sample_payload = {
        "key1": "value1",
        "key2": {"nested_key": "target_keyword"},
        "key3": ["list_item1", "list_item2", {"nested_list_key": "target_keyword"}]
    }
    target_keyword = "target_keyword"
    print(find_keyword_in_json(sample_payload, target_keyword))