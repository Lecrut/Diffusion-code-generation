def check_even(number):
    if not isinstance(number, int) or isinstance(number, bool):
        return "ERROR_INVALID_INPUT"
    return number % 2 == 0

if __name__ == '__main__':
    print(check_even(10))
    print(check_even(7))
    print(check_even(0))
    print(check_even(-3))
    print(check_even("2"))
    print(check_even(3.5))
    print(check_even(True))