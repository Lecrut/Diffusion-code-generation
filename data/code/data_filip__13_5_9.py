from functools import reduce

def snake_to_camel(snake_str: str) -> str:
    return reduce(lambda acc, part: acc + part.capitalize(), snake_str.split('_'))

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('snake_case_to_camel_case'))
    print(snake_to_camel('a'))