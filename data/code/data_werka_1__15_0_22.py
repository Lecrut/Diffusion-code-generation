def check_match(value1, value2):
    return value1 == value2
if __name__ == '__main__':
    print(check_match(42, 42))
    print(check_match('hello', 'hello'))
    print(check_match([1, 2, 3], [1, 2, 3]))
    print(check_match(42, 43))
    print(check_match('hello', 'world'))
    print(check_match([1, 2, 3], [3, 2, 1]))