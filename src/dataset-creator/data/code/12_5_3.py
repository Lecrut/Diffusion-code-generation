def is_odd(n):
    return isinstance(n, int) and (n & 1) != 0
if __name__ == '__main__':
    samples = [-5, -4, 3, 2, 7]
    for sample in samples:
        print(f"{sample}: {is_odd(sample)}")