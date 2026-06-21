def snake_to_camel(snake_string: str) -> str:
    parts = snake_string.split("_")
    if not parts:
        return ""
    first_word = parts[0]
    rest_words = [part.capitalize() for part in parts[1:] if part]
    return first_word + "".join(rest_words)

if __name__ == '__main__':
    input_string = "hello_world_example"
    result = snake_to_camel(input_string)
    print(result)