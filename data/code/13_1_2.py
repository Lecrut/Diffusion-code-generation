import re

def snake_to_camel(identifier):
    pattern = re.compile(r'_([a-zA-Z0-9])')
    return pattern.sub(lambda match: match.group(1).upper(), identifier)

if __name__ == '__main__':
    result = snake_to_camel("hello_world_example")
    print(result)
    result2 = snake_to_camel("foo_bar_baz")
    print(result2)
    result3 = snake_to_camel("simple")
    print(result3)