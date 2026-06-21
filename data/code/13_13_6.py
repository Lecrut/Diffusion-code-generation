def snake_to_camel(s):
    return ''.join(word.capitalize() if i else word for i, word in enumerate(s.split('_')))

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('snake_case_to_camel_case'))
    print(snake_to_camel('alreadyCamel'))
    print(snake_to_camel('single'))