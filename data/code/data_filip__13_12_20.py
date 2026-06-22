def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    samples = [
        'hello_world',
        'this_is_snake_case',
        'alreadycamel',
        'single',
        'a_b_c_d_e'
    ]
    for sample in samples:
        print(snake_to_camel(sample))