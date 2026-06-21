import json

def parse_json_like(json_string):
    return json.loads(json_string)

if __name__ == '__main__':
    sample_string = '{"a": 1, "b": {"c": 2}}'
    parsed_data = parse_json_like(sample_string)
    print(parsed_data)