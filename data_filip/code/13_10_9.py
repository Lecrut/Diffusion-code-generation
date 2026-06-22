import re

def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)

if __name__ == '__main__':
    print(snake_to_camel("hello_world"))
    print(snake_to_camel("this_is_a_test"))
    print(snake_to_camel("alreadyCamel"))
    print(snake_to_camel("multiple___underscores"))
    print(snake_to_camel("trailing_"))
    print(snake_to_camel("leading_"))
    print(snake_to_camel(""))
    print(snake_to_camel("single"))