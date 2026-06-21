def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    samples = ['hello_world', 'foo_bar_baz', 'alreadyCamel', 'single', 'two_words']
    for sample in samples:
        print(snake_to_camel(sample))