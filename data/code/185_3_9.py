def parse_json_like(json_string):
    def parse_value(value):
        if value.isdigit():
            return int(value)
        elif value.startswith('"') and value.endswith('"'):
            return value[1:-1]
        elif value == 'true':
            return True
        elif value == 'false':
            return False
        elif value == 'null':
            return None
        else:
            raise ValueError(f"Invalid JSON-like value: {value}")

    def parse_dict(d):
        result = {}
        for item in d.split(','):
            key, val = item.split(':')
            result[key.strip()] = parse_value(val.strip())
        return result

    def parse_list(l):
        return [parse_value(item.strip()) for item in l[1:-1].split(',')]

    if json_string.startswith('{'):
        return parse_dict(json_string)
    elif json_string.startswith('['):
        return parse_list(json_string)
    else:
        raise ValueError(f"Invalid JSON-like structure: {json_string}")

if __name__ == '__main__':
    sample_string = '{"a": "1", "b": [2, 3], "c": {"d": true}}'
    result = parse_json_like(sample_string)
    print(result)