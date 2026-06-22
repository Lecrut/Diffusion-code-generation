import re

def snake_to_camel(name: str) -> str:
    return re.sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), name)

if __name__ == '__main__':
    print(snake_to_camel("hello_world"))
    print(snake_to_camel("this_is_a_test"))
    print(snake_to_camel("alreadyCamel"))