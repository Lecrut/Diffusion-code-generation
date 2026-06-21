def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return snake_str
    parts = snake_str.split('_')
    first = parts[0]
    rest = parts[1:]
    if not rest:
        return first
    result = first + ''.join(word.capitalize() for word in rest)
    return result

if __name__ == '__main__':
    print(snake_to_camel('my_variable_name'))
    print(snake_to_camel('alreadyCamel'))
    print(snake_to_camel(''))
    print(snake_to_camel('single'))