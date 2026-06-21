def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

if __name__ == '__main__':
    sample_values = ['hello_world', 'foo_bar_baz', 'simple', 'a_b_c_d_e']
    for val in sample_values:
        print(snake_to_camel(val))