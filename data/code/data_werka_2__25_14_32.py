def is_zero(value):
    if isinstance(value, (int, float)):
        return value == 0
    elif isinstance(value, complex):
        return value == 0 + 0j
    else:
        raise ValueError('Unsupported data type')
if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero(0 + 0j))
    print(is_zero(1))
    print(is_zero(1.0))
    print(is_zero(1 + 0j))