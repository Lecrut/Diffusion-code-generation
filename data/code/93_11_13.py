def both_false(a: bool, b: bool) -> bool:
    neg_a = not a
    neg_b = not b
    return neg_a and neg_b

if __name__ == '__main__':
    x = True
    y = False
    result = both_false(x, y)
    print(result)
    x = False
    y = False
    result = both_false(x, y)
    print(result)