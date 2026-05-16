def calculate_non_negative_difference(len1, len2):
    if len1 > len2:
        return len1 - len2
    else:
        return len2 - len1
if __name__ == '__main__':
    a = 10
    b = 5
    print(calculate_non_negative_difference(a, b))
    c = 3
    d = 12
    print(calculate_non_negative_difference(c, d))
    e = 7
    f = 7
    print(calculate_non_negative_difference(e, f))