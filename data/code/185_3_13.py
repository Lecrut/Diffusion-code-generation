import json

def parse_json_like_string(json_str):
    return json.loads(json_str)

if __name__ == '__main__':
    sample_json = '{"name": "John", "age": 30, "children": [{"name": "Jane", "age": 10}]}'
    result = parse_json_like_string(sample_json)
    print(result)