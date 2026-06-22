def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    words = snake_str.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])

if __name__ == '__main__':
    result = snake_to_camel("hello_world_test")
    print(result)