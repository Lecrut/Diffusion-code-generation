def snake_to_camel(s):
    return ''.join(word.capitalize() if i else word for i, word in enumerate(s.split('_')) if word)

if __name__ == '__main__':
    sample = 'snake_case_variable_name'
    print(snake_to_camel(sample))