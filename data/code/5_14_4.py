def diff_length(len1, len2):
    if len1 > len2:
        return len1 - len2
    else:
        return len2 - len1
if __name__ == '__main__':
    a = 10
    b = 5
    print(diff_length(a, b))
    c = 3
    d = 8
    print(diff_length(c, d))