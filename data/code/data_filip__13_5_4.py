def snake_to_camel(s: str) -> str:
    parts = s.split('_')
    return parts[0] + ''.join(w.capitalize() for w in parts[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))