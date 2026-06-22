def snake_to_camel(text: str) -> str:
    parts = text.split('_')
    if not parts:
        return ''
    first = parts[0]
    rest = [part.capitalize() for part in parts[1:] if part]
    return first + ''.join(rest)

if __name__ == '__main__':
    print(snake_to_camel('get_element_by_id'))
    print(snake_to_camel('simple'))
    print(snake_to_camel('alreadyCamel'))