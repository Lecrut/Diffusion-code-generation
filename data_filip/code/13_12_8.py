def snake_to_camel(s: str) -> str:
    if not s:
        return s
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    input_str = "hello_world_example"
    result = snake_to_camel(input_str)
    print(result)