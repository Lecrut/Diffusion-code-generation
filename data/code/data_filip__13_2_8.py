def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    filtered_parts = [part for part in parts if part]
    if not filtered_parts:
        return ""
    first_part = filtered_parts[0]
    remaining_parts = [part.capitalize() for part in filtered_parts[1:]]
    return first_part + ''.join(remaining_parts)

if __name__ == '__main__':
    print(snake_to_camel("hello_world"))
    print(snake_to_camel("alreadyCamel"))
    print(snake_to_camel("__leading_underscores"))
    print(snake_to_camel("trailing_underscores__"))
    print(snake_to_camel("multiple___underscores"))
    print(snake_to_camel("single"))
    print(snake_to_camel("_"))
    print(snake_to_camel("__"))
    print(snake_to_camel(""))