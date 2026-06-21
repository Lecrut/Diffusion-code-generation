def to_camel_case(snake_str):
    if not snake_str:
        return ""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_input = "this_is_a_test_string"
    result = to_camel_case(sample_input)
    print(result)