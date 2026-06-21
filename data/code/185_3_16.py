def parse_json_like(json_string):
    def parse_value(value_str):
        if value_str.isdigit():
            return int(value_str)
        elif value_str.startswith('"') and value_str.endswith('"'):
            return value_str[1:-1]
        else:
            raise ValueError(f"Invalid value: {value_str}")

    def parse_object(obj_str):
        obj_str = obj_str.strip('{}')
        items = [item.split(':') for item in obj_str.split(',')]
        return {key.strip(): parse_value(value.strip()) for key, value in items}

    def parse_array(arr_str):
        arr_str = arr_str.strip('[]')
        items = [parse_value(item.strip()) for item in arr_str.split(',')]
        return items

    if json_string.startswith('{'):
        return parse_object(json_string)
    elif json_string.startswith('['):
        return parse_array(json_string)
    else:
        return parse_value(json_string)

if __name__ == '__main__':
    sample_string = '{"a": "10", "b": [25, 30], "c": {"d": 45}}'
    result = parse_json_like(sample_string)
    print(result)