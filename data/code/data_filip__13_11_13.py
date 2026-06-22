def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    if len(parts) == 1:
        return parts[0]
    return parts[0] + ''.join(part.capitalize() for part in parts[1:])

if __name__ == '__main__':
    samples = [
        'hello_world',
        'foo_bar_baz',
        'alreadyCamel',
        'single',
        '_leading_underscore',
        'trailing_underscore_',
        '__double__underscores__',
        'a_b_c_d_e_f_g_h_i_j_k',
        '',
        'simple'
    ]
    for sample in samples:
        print(snake_to_camel(sample))