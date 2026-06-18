def is_odd(n):
    return isinstance(n, int) and (n & 1) != 0
if __name__ == '__main__':
    samples = [5, -3, 42, 7]
    for num in samples:
        print(f"{num}: {is_odd(num)}")