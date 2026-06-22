def snake_to_camel(snake_str):
    if not snake_str:
        return snake_str
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_cases = ['hello_world', 'this_is_a_test', 'snake_case_conversion', 'single', 'alreadyCamel', 'multiple___underscores']
    for case in sample_cases:
        result = snake_to_camel(case)
        print(f"{case} -> {result}")