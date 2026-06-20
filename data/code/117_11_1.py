def abs_diff(a, b):
    return a if a > b else b

if __name__ == '__main__':
    print(abs_diff(10, 5))
    print(abs_diff(-3, -7))
    print(abs_diff(0, 0))
    print(abs_diff(2**64 - 1, 1))