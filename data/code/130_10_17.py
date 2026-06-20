def is_zero(number):
    if not isinstance(number, (int, float)):
        raise ValueError('Input must be an integer or float')
    return number == 0
if __name__ == '__main__':
    print(f'is_zero(0): {is_zero(0)}')
    print(f'is_zero(5): {is_zero(5)}')
    try:
        print(f'is_zero(-0): {is_zero(-0)}')
    except ValueError as e:
        print(e)
    print(f'is_zero(3.14): {is_zero(3.14)}')
    try:
        print(f"is_zero('0'): {is_zero('0')}")
    except ValueError as e:
        print(e)