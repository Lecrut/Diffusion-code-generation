def is_zero(value):
    if isinstance(value, (int, float)):
        return value == 0
    elif isinstance(value, str):
        return value.strip() == '0' or value.strip().lower() in ('zero', 'o')
    elif isinstance(value, bool):
        return not value
    else:
        raise ValueError(f'Unsupported type: {type(value)}')
if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero('0'))
    print(is_zero('zero'))
    print(is_zero('Zero'))
    print(is_zero('O'))
    print(is_zero(False))
    print(is_zero(True))
    print(is_zero(None))