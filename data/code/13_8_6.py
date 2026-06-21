def snake_to_camel(snake_str):
    words = snake_str.split('_')
    if not words:
        return ''
    return words[0] + ''.join(word.capitalize() for word in words[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('this_is_a_test'))
    print(snake_to_camel('alreadyCamel'))
    print(snake_to_camel('single'))
    print(snake_to_camel('with__double_underscores'))