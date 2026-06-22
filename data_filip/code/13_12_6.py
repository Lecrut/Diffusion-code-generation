def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return snake_str
    result = []
    words = snake_str.split('_')
    for i, word in enumerate(words):
        if i == 0:
            result.append(word)
        else:
            result.append(word[0].upper() + word[1:])
    return ''.join(result)

def camel_to_snake(camel_str: str) -> str:
    if not camel_str:
        return camel_str
    result = []
    for i, char in enumerate(camel_str):
        if char.isupper():
            if i > 0 and camel_str[i - 1].islower():
                result.append('_')
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)
if __name__ == '__main__':
    sample_snake = 'hello_world_test_case'
    sample_camel = 'helloWorldTestCase'
    snake_to_camel_result = snake_to_camel(sample_snake)
    print(snake_to_camel_result)
    camel_to_snake_result = camel_to_snake(sample_camel)
    print(camel_to_snake_result)
    test_snake = 'already_camel'
    test_camel = 'AlreadyCamel'
    snake_to_camel_test = snake_to_camel(test_snake)
    print(snake_to_camel_test)
    camel_to_snake_test = camel_to_snake(test_camel)
    print(camel_to_snake_test)
    edge_case = 'single_word'
    print(snake_to_camel(edge_case))
    empty = ''
    print(snake_to_camel(empty))
    multiple_underscores = 'hello___world'
    print(snake_to_camel(multiple_underscores))