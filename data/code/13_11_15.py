def snake_to_camel(snake_str):
    if not snake_str:
        return snake_str
    parts = snake_str.split('_')
    result = parts[0]
    for i in range(1, len(parts)):
        if parts[i]:
            result += parts[i].capitalize()
        else:
            result += '_'
    return result

if __name__ == '__main__':
    print(snake_to_camel('this_is_a_snake_case_string'))
    print(snake_to_camel('alreadyCamel'))
    print(snake_to_camel('_leading_underscore'))
    print(snake_to_camel(''))