def is_even(n):
    return n % 2 == 0

if __name__ == '__main__':
    samples = [2, 3, 0, -4]
    for val in samples:
        print(is_even(val))