def snake_to_camel(s: str) -> str:
    if not s:
        return s
    parts = s.split('_')
    if not parts:
        return s
    first = parts[0]
    rest = [part.capitalize() for part in parts[1:] if part]
    return first + ''.join(rest)

if __name__ == '__main__':
    result = snake_to_camel("hello_world_example")
    print(result)
    
    result2 = snake_to_camel("this_is_a_test")
    print(result2)
    
    result3 = snake_to_camel("single")
    print(result3)
    
    result4 = snake_to_camel("alreadyCamel")
    print(result4)
    
    result5 = snake_to_camel("_leading_underscore")
    print(result5)