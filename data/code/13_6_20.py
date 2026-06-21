def snake_to_camel(s: str) -> str:
    parts = s.split('_')
    if not parts:
        return ''
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample1 = 'hello_world'
    sample2 = 'convert_this_string'
    sample3 = 'alreadycamel'
    sample4 = ''
    sample5 = 'single'
    print(snake_to_camel(sample1))
    print(snake_to_camel(sample2))
    print(snake_to_camel(sample3))
    print(snake_to_camel(sample4))
    print(snake_to_camel(sample5))