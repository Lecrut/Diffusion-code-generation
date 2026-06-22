def snake_to_camel(snake_str):
    return ''.join([part.capitalize() if i else part for i, part in enumerate(snake_str.split('_'))])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('this_is_snake_case'))
    print(snake_to_camel('single'))
    print(snake_to_camel('a_b_c_d'))