def abs_diff(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return (a - b) & ((a - b) >> 31)

if __name__ == '__main__':
    print(abs_diff(1234567890123456789, 9876543210987654321))