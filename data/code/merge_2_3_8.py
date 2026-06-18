def is_even(n):
    return (n & 1) == 0
if __name__ == '__main__':
    samples = [0, -5, 42, -8]
    for val in samples:
        print(f"{val}: {is_even(val)}")