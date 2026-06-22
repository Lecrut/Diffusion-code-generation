from functools import reduce

def snake_to_camel(s: str) -> str:
    return reduce(lambda acc, part: acc + part.capitalize(), s.split('_'))[0].lower() + reduce(lambda acc, part: acc + part.capitalize(), s.split('_'))[1:] if s else ''

if __name__ == '__main__':
    samples = ['hello_world', 'user_name', 'first_name_last_name', 'single']
    for sample in samples:
        print(snake_to_camel(sample))