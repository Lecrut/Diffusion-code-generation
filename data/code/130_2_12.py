def is_zero(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Invalid input type. Expected int or float.")
    return value == 0

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero(-0))
    print(is_zero(-0.0))
    try:
        print(is_zero('a'))
    except ValueError as e:
        print(e)