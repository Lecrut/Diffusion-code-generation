def is_zero(value):
    def validate_input(val):
        if not isinstance(val, (int, float, complex)):
            raise ValueError('Unsupported data type')
    
    validate_input(value)
    
    if isinstance(value, int):
        return value == 0
    elif isinstance(value, float):
        return value == 0.0
    elif isinstance(value, complex):
        return value == 0 + 0j

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero(0 + 0j))
    try:
        print(is_zero('0'))
    except ValueError as e:
        print(e)
    try:
        print(is_zero(None))
    except ValueError as e:
        print(e)