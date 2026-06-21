def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('foo_bar_baz'))
    print(snake_to_camel('single'))
    print(snake_to_camel('a_b_c_d_e'))