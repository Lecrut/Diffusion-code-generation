def to_camel_case(snake_str: str) -> str:
    if not isinstance(snake_str, str):
        raise TypeError("Input must be a string")
    if not snake_str:
        return ""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_snake = "this_is_a_test_string"
    result = to_camel_case(sample_snake)
    print(result)
    sample_snake_empty = ""
    result_empty = to_camel_case(sample_snake_empty)
    print(result_empty)
    sample_snake_single = "single"
    result_single = to_camel_case(sample_snake_single)
    print(result_single)