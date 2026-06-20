import re

def is_alphanumeric(s):
    return bool(re.match('^[a-zA-Z0-9]+$', s))
if __name__ == '__main__':
    print(is_alphanumeric('Hello123'))
    print(is_alphanumeric('Hello 123'))