def compare_lengths(len1, len2):
    if len1 > len2:
        return {"length1": str(len1), "length2": str(len2), "greater": True}
    elif len2 > len1:
        return {"length1": str(len1), "length2": str(len2), "greater": False}
    else:
        return {"length1": str(len1), "length2": str(len2), "greater": False}
if __name__ == '__main__':
    a = 10
    b = 25
    result1 = compare_lengths(a, b)
    print(result1)
    c = 50
    d = 50
    result2 = compare_lengths(c, d)
    print(result2)
    e = 100
    f = 10
    result3 = compare_lengths(e, f)
    print(result3)