def is_zero(value):
    TOLERANCE = 1e-308
    return abs(value) < TOLERANCE

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(1))
    print(is_zero(-0.0))
    print(is_zero(0.0001))
    print(is_zero('0'))