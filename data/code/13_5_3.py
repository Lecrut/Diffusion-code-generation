def snake_to_camel(s):
    return s.replace('_', ' ').title().replace(' ', '')

if __name__ == '__main__':
    samples = ['hello_world', 'foo_bar_baz', 'test_case', 'alreadyCamel', 'single']
    for sample in samples:
        print(snake_to_camel(sample))