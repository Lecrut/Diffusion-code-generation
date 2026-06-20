def check_zero(value):
    if isinstance(value, (int, float)):
        return value == 0
    else:
        raise TypeError('Input must be a number')
if __name__ == '__main__':
    print(check_zero(0))
    print(check_zero(-1))
    print(check_zero(1.0))
    print(check_zero('0'))