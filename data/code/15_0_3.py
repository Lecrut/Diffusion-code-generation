def check_match(value1, value2):
    return value1 == value2
if __name__ == '__main__':
    print(check_match(10, 10))
    print(check_match(5, 3))
    print(check_match("hello", "hello"))
    print(check_match(True, True))
    print(check_match(1.5, 1.50))