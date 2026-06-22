def snake_to_camel(s):
    parts = s.split('_')
    if not parts:
        return s
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    samples = [
        'hello_world',
        'snake_case_string',
        'alreadyCamel',
        'single',
        'multiple_words_here',
        '_leading_underscore',
        'trailing_underscore_',
        '__double__underscores__',
        '',
        'no_underscores'
    ]
    for sample in samples:
        print(snake_to_camel(sample))