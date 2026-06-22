def snake_to_camel(s):
    return s[0] + ''.join(w.capitalize() for w in s[1:].split('_')) if '_' in s else s

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('first_name'))
    print(snake_to_camel('alreadyCamel'))
    print(snake_to_camel('a_b_c_d'))
    print(snake_to_camel('simple'))