def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return ""
    
    words = snake_str.split('_')
    camel_words = [words[0].lower()] + [word.capitalize() for word in words[1:] if word]
    return ''.join(camel_words)

if __name__ == '__main__':
    result = snake_to_camel("this_is_a_snake_case_string")
    print(result)