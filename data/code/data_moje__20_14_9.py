def check_parity(value):
    if not isinstance(value, int) or isinstance(value, bool):
        return "ERROR_INVALID_TYPE"
    return value % 2 == 0

if __name__ == '__main__':
    print(check_parity(4))
    print(check_parity(7))
    print(check_parity(0))
    print(check_parity("text"))
    print(check_parity(3.14))
    print(check_parity(True))