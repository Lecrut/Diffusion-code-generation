def compare_three(a, b, c):
    if a < b:
        ab = (a, b)
    else:
        ab = (b, a)
    if b < c:
        bc = (b, c)
    else:
        bc = (c, b)
    if a < c:
        ac = (a, c)
    else:
        ac = (c, a)
    results = sorted([ab, bc, ac])
    return tuple(results)
if __name__ == '__main__':
    print(compare_three(1, 2, 3))
    print(compare_three(5, 1, 4))
    print(compare_three(10, 20, 30))
    print(compare_three(7, 7, 7))
    print(compare_three(3, 1, 2))