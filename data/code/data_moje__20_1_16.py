PARITY_MAP = {0: True, 1: False}

def is_even(n):
    return PARITY_MAP[n & 1]

if __name__ == '__main__':
    samples = [10, 11, 0, -5, 42]
    output = [is_even(s) for s in samples]
    print(output)