def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    if len(parts) == 1:
        return parts[0]
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('this_is_a_test'))
    print(snake_to_camel('already_camel'))
    print(snake_to_camel('single'))
    print(snake_to_camel('two_words'))