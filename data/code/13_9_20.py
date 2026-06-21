def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if not components:
        return ''
    first = components[0]
    rest = [c.capitalize() for c in components[1:]]
    return ''.join([first] + rest)

if __name__ == '__main__':
    samples = ['hello_world', 'snake_case_to_camel', 'single', 'a_b_c_d', 'with_numbers_123']
    for s in samples:
        print(snake_to_camel(s))