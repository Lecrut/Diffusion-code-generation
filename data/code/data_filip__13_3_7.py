def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_snake = "this_is_a_test_string"
    result = snake_to_camel(sample_snake)
    print(result)
    another_sample = "single_word"
    print(snake_to_camel(another_sample))
    mixed_sample = "convert_this_snake_case"
    print(snake_to_camel(mixed_sample))