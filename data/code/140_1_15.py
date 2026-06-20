def is_even(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('Input must be a non-negative integer')
    return n & 1 == 0
if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even(0))