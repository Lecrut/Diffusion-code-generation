def is_number_zero(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be an integer or float.")
    return value == 0

if __name__ == '__main__':
    print(is_number_zero(0))
    print(is_number_zero(0.0))
    try:
        print(is_number_zero('a'))
    except TypeError as e:
        print(e)