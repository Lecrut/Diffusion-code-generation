def check_parity(value):
    if not isinstance(value, int) or isinstance(value, bool):
        return "ERROR_INVALID_TYPE"
    if value % 2 == 0:
        return True
    return False

if __name__ == '__main__':
    print(check_parity(4))
    print(check_parity(7))
    print(check_parity(0))
    print(check_parity(-2))
    print(check_parity("hello"))
    print(check_parity(3.14))
    print(check_parity(True))