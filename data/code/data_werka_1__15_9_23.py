def check_match(value1, value2):
    return value1 == value2
if __name__ == '__main__':
    print(check_match(42, 42))
    print(check_match('hello', 'world'))
    print(check_match([1, 2, 3], [1, 2, 3]))
    print(check_match({'key': 'value'}, {'key': 'value'}))
    print(check_match(3.14, 2.71))