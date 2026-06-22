def to_camel_case(snake_str):
    parts = snake_str.split('_')
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part[0].upper() + part[1:]
    return result

if __name__ == '__main__':
    sample_snake = "this_is_an_example_string"
    print(to_camel_case(sample_snake))