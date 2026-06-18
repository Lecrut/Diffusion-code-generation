def is_odd(value):
    return isinstance(value, int) and (value & 1) != 0
if __name__ == '__main__':
    samples = [5, -3, 42, '7', 8]
    for item in samples:
        if is_odd(item):
            print(f"{item} is odd")