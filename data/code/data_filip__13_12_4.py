def snake_to_camel(snake_case_str):
    if not snake_case_str:
        return ""
    parts = snake_case_str.split('_')
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part[0].upper() + part[1:]
    return result

if __name__ == '__main__':
    sample_input = "this_is_a_test_string"
    converted_value = snake_to_camel(sample_input)
    print(converted_value)