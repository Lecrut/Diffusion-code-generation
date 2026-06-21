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
    sample_payload = {
        "name": "John",
        "age": 30,
        "children": [
            {"name": "Jane", "age": 10},
            {"name": "Doe", "age": 5}
        ],
        "address": {
            "street": "123 Main St",
            "city": "Anytown"
        }
    }
    keyword = "Jane"
    print(find_keyword_in_json(sample_payload, keyword))