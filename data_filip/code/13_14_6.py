def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if not components:
        return ''
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    samples = ['hello_world', 'foo_bar_baz', 'a_b', 'alreadycamel', 'single', 'under_score']
    for s in samples:
        print(snake_to_camel(s))