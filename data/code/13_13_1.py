def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_input = 'this_is_a_test_variable'
    result = snake_to_camel(sample_input)
    print(result)