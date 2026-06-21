def is_zero(value):
    zero_map = {
        int: 0,
        float: 0.0,
        complex: 0 + 0j,
    }
    
    value_type = type(value)
    if value_type in zero_map:
        return value == zero_map[value_type]
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
    try:
        print(is_zero(None))
    except ValueError as e:
        print(e)