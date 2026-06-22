def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    samples = [
        'hello_world',
        'snake_case_string',
        'alreadyCamel',
        'single_word',
        'two_words',
        'with_underscores__double',
        '_leading_underscore',
        'trailing_underscore_'
    ]
    for sample in samples:
        print(snake_to_camel(sample))