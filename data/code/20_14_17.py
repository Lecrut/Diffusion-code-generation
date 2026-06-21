def check_even(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return None
    return n % 2 == 0

if __name__ == '__main__':
    print(check_even(4))
    print(check_even(7))
    print(check_even(0))
    print(check_even(-3))
    print(check_even(2.5))
    print(check_even("5"))
    print(check_even(None))
    print(check_even(True))