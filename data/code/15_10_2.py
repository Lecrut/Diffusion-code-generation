def check_match(value1, value2):
    return value1 == value2
if __name__ == '__main__':
    print(check_match(5, 5))
    print(check_match(10, 5))
    print(check_match("hello", "hello"))
    print(check_match(1, 2))
    print(check_match(3.14, 3.14))