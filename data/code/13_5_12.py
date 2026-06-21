def snake_to_camel(s):
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(s.split('_')))

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))