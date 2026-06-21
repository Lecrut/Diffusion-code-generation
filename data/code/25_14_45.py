def is_zero(value):

    def check_int_or_float(val):
        return isinstance(val, (int, float)) and val == 0

    def check_complex(val):
        return isinstance(val, complex) and val == 0 + 0j
    if check_int_or_float(value) or check_complex(value):
        return True
    else:
        raise ValueError('Unsupported data type')
if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero(0 + 0j))
    try:
        print(is_zero('0'))
    except ValueError as e:
        print(e)
    print(is_zero(1))
    print(is_zero(1.5))
    print(is_zero(1 + 2j))