def snake_to_camel(snake_str):
    if not isinstance(snake_str, str):
        raise TypeError("Input must be a string")
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    result = snake_to_camel("this_is_a_snake_case_string")
    print(result)