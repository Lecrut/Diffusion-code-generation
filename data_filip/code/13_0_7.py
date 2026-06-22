def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_snake = "this_is_a_test_string"
    result = to_camel_case(sample_snake)
    print(result)
    sample_snake_2 = "another_example"
    result_2 = to_camel_case(sample_snake_2)
    print(result_2)
    sample_snake_3 = "singleword"
    result_3 = to_camel_case(sample_snake_3)
    print(result_3)