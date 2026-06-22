def snake_to_camel(s):
    return ''.join(word.capitalize() if i else word for i, word in enumerate(s.split('_')) if word)

if __name__ == '__main__':
    result = snake_to_camel('hello_world_example')
    print(result)