def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if not components:
        return ''
    first = components[0]
    rest = ''.join(word.capitalize() for word in components[1:])
    return first + rest

if __name__ == '__main__':
    sample_values = [
        'hello_world',
        'snake_case_example',
        'alreadyCamel',
        'single',
        'multiple__underscores',
        '_leading',
        'trailing_',
        '__both__',
        'a_b_c',
        'get_http_response_code'
    ]
    for val in sample_values:
        print(snake_to_camel(val))