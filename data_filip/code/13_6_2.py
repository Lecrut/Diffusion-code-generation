def snake_to_camel(snake_str: str) -> str:
    parts = snake_str.split('_')
    if not parts:
        return ''
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample = 'hello_world_foo_bar'
    result = snake_to_camel(sample)
    print(result)