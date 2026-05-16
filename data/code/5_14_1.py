def length_difference(len1, len2):
    if len1 > len2:
        return len1 - len2
    else:
        return len2 - len1
if __name__ == '__main__':
    a = 10
    b = 4
    print(length_difference(a, b))
    x = 5
    y = 15
    print(length_difference(x, y))
    p = 7
    q = 7
    print(length_difference(p, q))