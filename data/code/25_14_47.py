def is_zero(value):
    def validate_number(num):
        if not isinstance(num, (int, float)):
            raise ValueError('Unsupported data type')
    
    def validate_complex_num(cnum):
        if not isinstance(cnum, complex):
            raise ValueError('Unsupported data type')
    
    if isinstance(value, (int, float)):
        validate_number(value)
        return value == 0
    elif isinstance(value, complex):
        validate_complex_num(value)
        return value == 0 + 0j
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
    try:
        print(is_zero(None))
    except ValueError as e:
        print(e)