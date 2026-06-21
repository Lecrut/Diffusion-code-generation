def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if len(components) == 1:
        return components[0]
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    samples = [
        'hello_world',
        'snake_case_to_camel',
        'alreadyCamel',
        'single',
        'a_b_c_d',
        'leading_and_trailing__',
        '_starts_with_underscore',
        'ends_with_underscore_',
        'multiple___underscores',
        'simple',
        'two_words'
    ]
    for sample in samples:
        print(f"{sample} -> {snake_to_camel(sample)}")