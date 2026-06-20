def is_even(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError('Input must be a non-negative integer.')
    return number & 1 == 0
if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))