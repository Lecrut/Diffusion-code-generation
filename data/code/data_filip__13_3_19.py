def snake_to_camel(s: str) -> str:
    if not s:
        return s
    
    parts = s.split('_')
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part.capitalize()
        else:
            result += '_'
    return result

if __name__ == '__main__':
    print(snake_to_camel("hello_world"))
    print(snake_to_camel("my_variable_name"))
    print(snake_to_camel("alreadyCamelCase"))
    print(snake_to_camel("double__underscore"))
    print(snake_to_camel(""))
    print(snake_to_camel("single"))