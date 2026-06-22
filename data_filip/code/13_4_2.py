import re

def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    print(snake_to_camel('get_user_data'))