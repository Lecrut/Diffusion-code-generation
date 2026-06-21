def snake_to_camel(snake_str):
    if not snake_str:
        return snake_str
    parts = snake_str.split('_')
    if len(parts) == 1:
        return parts[0]
    first = parts[0]
    rest = [word.capitalize() for word in parts[1:]]
    return first + ''.join(rest)

if __name__ == '__main__':
    sample_snake_cases = ['hello_world', 'my_variable_name', 'single', 'a_b_c_d', '']
    for s in sample_snake_cases:
        print(snake_to_camel(s))