def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_input = "this_is_a_test_string"
    result = snake_to_camel(sample_input)
    print(result)
    sample_input_2 = "another_example"
    result_2 = snake_to_camel(sample_input_2)
    print(result_2)
    sample_input_3 = "single"
    result_3 = snake_to_camel(sample_input_3)
    print(result_3)