def is_numerically_zero(value):
    return value == 0 or (isinstance(value, float) and abs(value) < 1e-09)
if __name__ == '__main__':
    print(is_numerically_zero(0))
    print(is_numerically_zero(-0.0))
    print(is_numerically_zero(1e-10))
    print(is_numerically_zero(1))
    print(is_numerically_zero('0'))