def abs_diff(a, b):
    return ((a - b) ^ (a - b >> 31)) - (a - b >> 31)

if __name__ == '__main__':
    print(abs_diff(5, 3))
    print(abs_diff(-4, 2))
    print(abs_diff(0, 0))