def is_odd(x):
    return isinstance(x, int) and (x & 1) != 0
if __name__ == '__main__':
    samples = [-5, -2, 3, 4, 7]
    for val in samples:
        print(f"{val}: {is_odd(val)}")