def check_match(value1, value2):
    return value1 == value2
if __name__ == '__main__':
    print(check_match(42, 42))
    print(check_match('hello', 'hello'))
    print(check_match(3.14, 3.14159))
    print(check_match(True, False))