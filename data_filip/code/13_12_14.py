def to_camel_case(snake_str):
    if not snake_str:
        return ""
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

if __name__ == '__main__':
    test_cases = ['hello_world', 'this_is_a_test', 'snake_case', 'a', 'alreadyCamel', 'multiple___underscores']
    for case in test_cases:
        print(to_camel_case(case))