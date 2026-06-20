def is_zero(number):
    if not isinstance(number, (int, float)):
        raise ValueError('Input must be an integer or float')
    return number == 0
if __name__ == '__main__':
    try:
        print(is_zero(0))
        print(is_zero(5))
        print(is_zero(-10))
        print(is_zero('a'))
    except ValueError as e:
        print(e)