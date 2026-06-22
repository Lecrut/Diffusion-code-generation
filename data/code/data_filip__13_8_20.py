def to_camel_case(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_strings = ['hello_world', 'this_is_a_test', 'snake_case_conversion']
    for s in sample_strings:
        print(to_camel_case(s))