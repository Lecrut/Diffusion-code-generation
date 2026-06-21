import re

def snake_to_camel(s):
    pattern = re.compile(r'_[a-zA-Z]')
    return pattern.sub(lambda match: match.group(0)[1].upper(), s)

if __name__ == '__main__':
    result = snake_to_camel("snake_case_string")
    print(result)