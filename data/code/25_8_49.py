def is_zero(value):
    if isinstance(value, (int, float)):
        return value == 0
    return False
if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(1))
    print(is_zero(-0.0))
    print(is_zero(0.0001))
    print(is_zero('0'))