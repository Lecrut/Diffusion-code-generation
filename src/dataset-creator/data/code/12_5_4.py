def is_odd(value):
    return isinstance(value, int) and (value & 1) != 0
if __name__ == '__main__':
    samples = [5, -3, 42, 7]
    for num in samples:
        print(f"{num}: {is_odd(num)}")