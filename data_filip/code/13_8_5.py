def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])

if __name__ == '__main__':
    samples = ['hello_world', 'foo_bar_baz', 'simple', 'already_Camel', 'two_words']
    for sample in samples:
        print(snake_to_camel(sample))