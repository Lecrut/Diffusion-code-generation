def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    samples = ['hello_world', 'foo_bar_baz', 'alreadyCamel', 'single', 'with__multiple__underscores']
    for s in samples:
        print(snake_to_camel(s))