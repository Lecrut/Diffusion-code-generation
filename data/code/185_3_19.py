def parse_json_like(json_string):
    import ast
    return ast.literal_eval(json_string)

if __name__ == '__main__':
    sample_string = '{"a": 1, "b": {"c": 2, "d": [3, 4]}, "e": 5}'
    parsed_data = parse_json_like(sample_string)
    print(parsed_data)