def is_odd(value):
    return isinstance(value, int) and (value & 1) != 0
if __name__ == '__main__':
    samples = [3, -5, 42, '7', 8]
    for item in samples:
        print(f"{item}: {is_odd(item)}")