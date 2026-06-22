import re

def snake_to_camel(identifier: str) -> str:
    parts = identifier.split('_')
    if not parts:
        return ''
    first = parts[0]
    rest = [word.capitalize() for word in parts[1:]]
    return first + ''.join(rest)

if __name__ == '__main__':
    sample = 'this_is_a_sample_string'
    result = snake_to_camel(sample)
    print(result)