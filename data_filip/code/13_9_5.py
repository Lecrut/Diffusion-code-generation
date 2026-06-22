def snake_to_camel(s):
    if not s:
        return ""
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world_example'))
    print(snake_to_camel('foo_bar'))
    print(snake_to_camel('simple'))
    print(snake_to_camel(''))