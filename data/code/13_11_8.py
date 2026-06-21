def snake_to_camel(identifier):
    parts = identifier.split('_')
    if not parts:
        return ''
    first = parts[0]
    rest = parts[1:]
    capitalized_rest = [word.capitalize() for word in rest]
    return first + ''.join(capitalized_rest)

if __name__ == '__main__':
    sample_snake = "hello_world_example"
    result = snake_to_camel(sample_snake)
    print(result)