def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = ['hello_world', 'user_profile_name', 'convert_this_string', 'singleword']
    for case in test_cases:
        print(to_camel_case(case))