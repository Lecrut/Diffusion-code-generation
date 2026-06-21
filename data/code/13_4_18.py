def snake_to_camel(s):
    parts = s.split('_')
    if len(parts) == 0:
        return ''
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    samples = [
        'hello_world',
        'this_is_a_test',
        'alreadyCamel',
        'single',
        'with_numbers_123',
        '',
        'multiple___underscores',
        'start_with_underscore',
        'end_with_underscore_',
        '_double_leading_',
        'a_b_c_d',
        'UPPER_CASE_test',
        'mixed_Case_Snake_Case'
    ]
    for sample in samples:
        print(snake_to_camel(sample))