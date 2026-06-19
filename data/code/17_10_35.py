def is_even(n):
    if not isinstance(n, int):
        raise ValueError('Input must be an integer')
    return n % 2 == 0
if __name__ == '__main__':
    try:
        print(is_even(10))
        print(is_even(3))
    except ValueError as e:
        print(e)