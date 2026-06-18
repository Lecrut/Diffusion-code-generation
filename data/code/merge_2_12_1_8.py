def check_parity(value):
    if isinstance(value, (int, float)):
        return value > 0 and int(value) % 2 != 0
    return False
if __name__ == '__main__':
    print(check_parity(3))
    print(check_parity(-5))
    print(check_parity(4.1))
    print(check_parity(7))