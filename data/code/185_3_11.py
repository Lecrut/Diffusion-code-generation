import re

def parse_json_like(json_string):
    def parse_value(value_str):
        value_str = value_str.strip()
        if value_str.startswith('{'):
            return parse_dict(value_str)
        elif value_str.startswith('['):
            return parse_list(value_str)
        elif value_str.isdigit():
            return int(value_str)
        else:
            return value_str

    def parse_dict(dict_str):
        dict_str = dict_str[1:-1]
        pairs = re.split(r',\s*', dict_str)
        result = {}
        for pair in pairs:
            key, value = pair.split(':', 1)
            result[key.strip()] = parse_value(value.strip())
        return result

    def parse_list(list_str):
        list_str = list_str[1:-1]
        items = re.split(r',\s*', list_str)
        return [parse_value(item.strip()) for item in items]

    return parse_value(json_string)

if __name__ == '__main__':
    sample_string = '{"a": 1, "b": [2, 3], "c": {"d": 4}}'
    result = parse_json_like(sample_string)
    print(result)