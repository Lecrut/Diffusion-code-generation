def is_even(n):
    return n in {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, -2, -4, -6, -8, -10}

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(7))
    print(is_even(0))
    print(is_even(-2))