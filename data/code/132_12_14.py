def is_valid_boolean(value):
    return value.lower() in {'true', 'false', '1', '0'}
if __name__ == '__main__':
    print(is_valid_boolean('True'))
    print(is_valid_boolean('false'))
    print(is_valid_boolean('1'))
    print(is_valid_boolean('0'))
    print(is_valid_boolean('2'))
    print(is_valid_boolean('abc'))