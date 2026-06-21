def find_median(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c

if __name__ == '__main__':
    print(find_median(3, 1, 2))