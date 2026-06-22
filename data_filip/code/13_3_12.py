def snake_to_camel(snake_str: str) -> str:
    parts = snake_str.split('_')
    if not parts or (len(parts) == 1 and parts[0] == ''):
        return snake_str
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_snake_strings = [
        "hello_world",
        "user_profile_data",
        "single",
        "multiple___underscores",
        "_leading_trailing_"
    ]
    for s in sample_snake_strings:
        result = snake_to_camel(s)
        print(result)