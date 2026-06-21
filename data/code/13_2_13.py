def snake_to_camel(snake_str):
    if not snake_str:
        return snake_str
    
    parts = snake_str.split('_')
    
    leading_underscores = 0
    while parts and parts[0] == '':
        leading_underscores += 1
        parts.pop(0)
        
    trailing_underscores = 0
    while parts and parts[-1] == '':
        trailing_underscores += 1
        parts.pop()
        
    if not parts:
        return '_' * (leading_underscores + trailing_underscores)
        
    camel_parts = []
    for i, part in enumerate(parts):
        if part:
            if i == 0:
                camel_parts.append(part)
            else:
                camel_parts.append(part[0].upper() + part[1:])
                
    return '_' * leading_underscores + ''.join(camel_parts) + '_' * trailing_underscores

if __name__ == '__main__':
    test_cases = [
        'hello_world',
        'foo_bar_baz',
        '_leading_underscore',
        'trailing_underscore_',
        '__double__underscores__',
        'alreadyCamel',
        'single',
        '_start_and_end_',
        'a_b_c',
        '__empty___parts__',
        '_',
        '',
        'no_underscore',
        '___',
        'a',
        'A_B',
        'with_spaces  ',
        '123_456',
        '_private_method_',
        'get_user_name'
    ]
    
    for case in test_cases:
        result = snake_to_camel(case)
        print(repr(case) + ' -> ' + repr(result))