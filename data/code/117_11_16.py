def abs_diff(a, b):
    return a - b & a - b >> 31
if __name__ == '__main__':
    print(abs_diff(10, 5))
    print(abs_diff(-7, -3))
    print(abs_diff(0, 0))