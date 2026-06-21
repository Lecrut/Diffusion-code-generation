def is_even(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return n % 2 == 0

if __name__ == '__main__':
    samples = [0, 1, 2, -3, -4, 100, -101]
    for s in samples:
        print(is_even(s))