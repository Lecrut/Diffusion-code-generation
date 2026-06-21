def is_even(value):
    if not isinstance(value, int) or isinstance(value, bool):
        return "Invalid input: expected an integer"
    return value % 2 == 0

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even(-2))
    print(is_even(-3))
    print(is_even(0))
    print(is_even(3.14))
    print(is_even("hello"))
    print(is_even(True))
    print(is_even(None))