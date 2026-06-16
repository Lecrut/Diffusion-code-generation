def check_parity(value):
    if isinstance(value, (int, float)) and value > 0:
        return abs(int(value) % 2 != 0) == True
    return False
if __name__ == '__main__':
    print(check_parity(15))
    print(check_parity(-3.7))
    print(check_parity(4.0))
    print(check_parity(8))