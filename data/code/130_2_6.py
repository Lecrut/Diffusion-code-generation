def is_zero(value):
    zero_map = {0: True, 0.0: True}
    return value in zero_map

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero(-0))
    print(is_zero(-0.0))
    print(is_zero(1))
    print(is_zero(1.0))