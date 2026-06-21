def is_even(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    samples = [0, 1, 2, -1, -2, -3, 4, -4]
    for s in samples:
        print(is_even(s))