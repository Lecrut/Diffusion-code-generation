def snake_to_camel(name: str) -> str:
    if not name:
        return name
    parts = name.split('_')
    if not parts:
        return name
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part[0].upper() + part[1:]
    return result

if __name__ == '__main__':
    sample_input = "hello_world_example"
    result = snake_to_camel(sample_input)
    print(result)