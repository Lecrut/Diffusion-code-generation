import re

def snake_to_camel(text):
    words = text.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

if __name__ == '__main__':
    print(snake_to_camel('this_is_a_snake_case_string'))