def is_zero(value):
    zero_values = {0, -0.0, 0.0}
    return value in zero_values
if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(1))
    print(is_zero(-0.0))
    print(is_zero(0.0001))
    print(is_zero('0'))