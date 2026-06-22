def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    parts = snake_str.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_snake = "this_is_an_example"
    result = snake_to_camel(sample_snake)
    print(result)