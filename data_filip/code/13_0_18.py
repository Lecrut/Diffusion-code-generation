def to_camel_case(snake_str: str) -> str:
    if not snake_str:
        return ""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_strings = ['hello_world', 'this_is_a_test', 'single', '_leading', 'trailing_', 'multiple___underscores']
    for s in sample_strings:
        print(to_camel_case(s))