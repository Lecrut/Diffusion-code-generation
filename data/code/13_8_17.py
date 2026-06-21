def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_input = "this_is_an_example_of_snake_case"
    result = snake_to_camel(sample_input)
    print(result)
    sample_input2 = "single"
    result2 = snake_to_camel(sample_input2)
    print(result2)
    sample_input3 = "a_b_c"
    result3 = snake_to_camel(sample_input3)
    print(result3)