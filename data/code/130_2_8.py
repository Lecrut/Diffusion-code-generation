def is_zero(value):
    return value == 0 or (isinstance(value, float) and abs(value) < 1e-9)

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero(-0))
    print(is_zero(-0.0))
    print(is_zero(1))
    print(is_zero(1.0))