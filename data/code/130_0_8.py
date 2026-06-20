def is_zero(value):
    return abs(value) < 1e-9

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(1e-10))
    print(is_zero(-1e-10))
    print(is_zero(1e-8))