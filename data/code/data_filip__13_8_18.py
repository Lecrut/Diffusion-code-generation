def snake_to_camel(s):
    return ''.join(word.capitalize() if i else word.lower() for i, word in enumerate(s.split('_')))

if __name__ == '__main__':
    samples = ['hello_world', 'snake_case_string', 'another_example', 'foo_bar_baz']
    for sample in samples:
        print(snake_to_camel(sample))