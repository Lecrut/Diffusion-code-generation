def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_input = "convert_this_string_to_camel_case"
    result = snake_to_camel(sample_input)
    print(result)
    sample_input_two = "hello_world"
    result_two = snake_to_camel(sample_input_two)
    print(result_two)
    sample_input_three = "snake_case_example"
    result_three = snake_to_camel(sample_input_three)
    print(result_three)