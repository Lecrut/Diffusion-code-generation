def snake_to_camel(snake_str: str) -> str:
    result = []
    upper_next = False
    for char in snake_str:
        if char == '_':
            upper_next = True
        else:
            if upper_next:
                result.append(char.upper())
                upper_next = False
            else:
                result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    snake_input = "this_is_a_sample_string"
    output = snake_to_camel(snake_input)
    print(output)