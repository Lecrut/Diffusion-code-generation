def snake_to_camel(s):
    return ''.join(word.capitalize() if i else word for i, word in enumerate(s.split('_')))

if __name__ == '__main__':
    result = snake_to_camel('my_variable_name')
    print(result)