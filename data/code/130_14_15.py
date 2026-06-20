def is_zero(num):
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a number")
    return num == 0

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(42))
    print(is_zero(-1.5))
    try:
        print(is_zero('a'))
    except ValueError as e:
        print(e)