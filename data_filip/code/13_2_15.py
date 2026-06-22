def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    filtered_parts = [part for part in parts if part]
    if not filtered_parts:
        return ''
    first = filtered_parts[0]
    rest = [part.capitalize() for part in filtered_parts[1:]]
    result = first + ''.join(rest)
    leading_underscores = snake_str.count('_') - (len(parts) - 1) if parts else 0
    if leading_underscores > 0 and snake_str.startswith('_'):
        result = '_' * leading_underscores + result
    return result

if __name__ == '__main__':
    samples = [
        'simple_case',
        '__leading_underscore',
        'multiple___underscores',
        'already_camel',
        '',
        'single',
        '__double_leading',
        'trailing__',
        '_mixed__case_',
        'a_b_c'
    ]
    for sample in samples:
        print(snake_to_camel(sample))