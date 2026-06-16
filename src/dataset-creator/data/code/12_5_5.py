def is_odd(number):
    return isinstance(number, int) and (number & 1) != 0
if __name__ == '__main__':
    samples = [3, -5, 42, 7]
    for val in samples:
        print(f"{val}: {is_odd(val)}")