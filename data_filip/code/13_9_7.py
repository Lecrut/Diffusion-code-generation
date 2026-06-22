def snake_to_camel(snake_str):
    if not snake_str:
        return snake_str
    parts = snake_str.split('_')
    return parts[0] + ''.join(part.capitalize() for part in parts[1:])

if __name__ == '__main__':
    result = snake_to_camel('this_is_a_snake_case_string')
    print(result)