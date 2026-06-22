def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part[0].upper() + part[1:]
    return result

if __name__ == '__main__':
    sample_input = "this_is_a_test_string"
    output = snake_to_camel(sample_input)
    print(output)
    another_input = "hello_world"
    another_output = snake_to_camel(another_input)
    print(another_output)
    empty_input = ""
    empty_output = snake_to_camel(empty_input)
    print(empty_output)