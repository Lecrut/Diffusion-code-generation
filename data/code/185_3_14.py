import json

def parse_json_like(s):
    return json.loads(s)

if __name__ == '__main__':
    sample = '{"a": 1, "b": {"c": 2, "d": [3, 4]}, "e": 5}'
    result = parse_json_like(sample)
    print(result)