import re

def snake_to_camel(name: str) -> str:
    pattern = re.compile('_([a-zA-Z])')
    result = pattern.sub(lambda match: match.group(1).upper(), name)
    return result
if __name__ == '__main__':
    sample_snake_case = 'get_user_data'
    result = snake_to_camel(sample_snake_case)
    print(result)