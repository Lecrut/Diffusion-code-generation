def find_median(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return b

if __name__ == '__main__':
    print(find_median(3, 1, 2))