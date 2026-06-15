def get_median(a, b, c):
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c
if __name__ == '__main__':
    print(get_median(1, 5, 3))
    print(get_median(10, 2, 8))
    print(get_median(4, 7, 2))
    print(get_median(9, 1, 5))
    print(get_median(3, 3, 3))
    print(get_median(100, 50, 25))