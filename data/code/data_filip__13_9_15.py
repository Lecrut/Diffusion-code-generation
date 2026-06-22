def snake_to_camel(s: str) -> str:
    parts = s.split('_')
    return parts[0] + ''.join(part.capitalize() for part in parts[1:])

if __name__ == '__main__':
    result = snake_to_camel('hello_world')
    print(result)