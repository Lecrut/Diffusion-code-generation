def check_zero(value):
    if isinstance(value, (int, float)):
        return value == 0
    else:
        raise TypeError("Input must be a numeric type")

if __name__ == '__main__':
    print(check_zero(0))
    print(check_zero(1.0))
    print(check_zero(-0.0))
    try:
        print(check_zero('0'))
    except TypeError as e:
        print(e)