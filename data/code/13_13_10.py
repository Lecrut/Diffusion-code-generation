def snake_to_camel(snake_str):
    return ''.join(word.capitalize() for word in snake_str.split('_'))

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('foo_bar_baz'))
    print(snake_to_camel('single'))
    print(snake_to_camel('a_b_c_d_e'))