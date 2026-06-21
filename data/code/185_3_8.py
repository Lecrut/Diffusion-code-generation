import json

def parse_json_like_string(json_str):
    return json.loads(json_str)

if __name__ == '__main__':
    sample_json = '{"a": 1, "b": {"c": 2, "d": [3, 4]}}'
    result = parse_json_like_string(sample_json)
    print(result)