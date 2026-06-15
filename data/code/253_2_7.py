def get_median(a, b, c):
    if a <= b <= c or c <= b <= a:
        if a <= b <= c:
            return b
        else:
            return b
    elif b <= a <= c or c <= a <= b:
        if b <= a <= c:
            return a
        else:
            return a
    else:
        return c
if __name__ == '__main__':
    print(get_median(1, 5, 3))
    print(get_median(10, 2, 8))
    print(get_median(4, 9, 1))
    print(get_median(7, 7, 3))
    print(get_median(100, 50, 25))