def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    samples = [
        'hello_world',
        'foo_bar_baz',
        'alreadyCamel',
        'single_word',
        'leading_and_trailing__',
    ]
    for sample in samples:
        print(snake_to_camel(sample))