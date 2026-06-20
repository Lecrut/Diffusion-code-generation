def is_zero(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input must be an integer or a float")
    return value == 0

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(42))
    print(is_zero(-1))
    print(is_zero(3.14))
    try:
        print(is_zero('a'))
    except ValueError as e:
        print(e)