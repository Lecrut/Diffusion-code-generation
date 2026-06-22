def is_even(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return "ERROR"
    return n % 2 == 0

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even(0))
    print(is_even(-2))
    print(is_even(3.5))
    print(is_even("10"))
    print(is_even(True))