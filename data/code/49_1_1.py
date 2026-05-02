def compare_lengths(len1, len2):
    if len1 > len2:
        return {"length1": str(len1), "length2": str(len2), "greater": True}
    elif len2 > len1:
        return {"length1": str(len1), "length2": str(len2), "greater": False}
    else:
        return {"length1": str(len1), "length2": str(len2), "greater": False}
if __name__ == '__main__':
    l1 = 10
    l2 = 25
    result1 = compare_lengths(l1, l2)
    print(result1)
    l3 = 50
    l4 = 50
    result2 = compare_lengths(l3, l4)
    print(result2)
    l5 = 100
    l6 = 10
    result3 = compare_lengths(l5, l6)
    print(result3)