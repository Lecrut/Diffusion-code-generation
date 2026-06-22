def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    words = snake_str.split('_')
    if len(words) == 1:
        return words[0]
    result = words[0]
    for word in words[1:]:
        if word:
            result += word.capitalize()
    return result

if __name__ == '__main__':
    print(snake_to_camel("hello_world"))
    print(snake_to_camel("snake_case_string"))
    print(snake_to_camel("single"))
    print(snake_to_camel("alreadyCamel"))
    print(snake_to_camel(""))
    print(snake_to_camel("_leading_underscore"))
    print(snake_to_camel("trailing_underscore_"))