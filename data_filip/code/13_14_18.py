def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_inputs = [
        'hello_world',
        'foo_bar_baz',
        'alreadyCamel',
        'single',
        'with__double__underscores',
        '_leading',
        'trailing_',
        '__both__',
        'a_b_c_d_e',
        'get_http_response_code'
    ]
    for s in sample_inputs:
        print(snake_to_camel(s))