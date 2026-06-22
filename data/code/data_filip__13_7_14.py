def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        ("hello_world", "helloWorld"),
        ("already_Camel", "alreadyCamel"),
        ("single", "single"),
        ("multiple_words_here", "multipleWordsHere"),
        ("_leading_underscore", "LeadingUnderscore"),
        ("trailing_underscore_", "trailingUnderscore"),
        ("double__underscore", "doubleUnderscore")
    ]
    for snake_input, expected in test_cases:
        result = snake_to_camel(snake_input)
        print(f"{snake_input} -> {result} (expected: {expected})")