def compare_three(a, b, c):
    if a <= b:
        rel_ab = (a, b)
    else:
        rel_ab = (b, a)
    if b <= c:
        rel_bc = (b, c)
    else:
        rel_bc = (c, b)
    if a <= c:
        rel_ac = (a, c)
    else:
        rel_ac = (c, a)
    return (rel_ab, rel_bc, rel_ac)
if __name__ == '__main__':
    print(compare_three(1, 5, 3))
    print(compare_three(10, 20, 5))
    print(compare_three(7, 7, 7))
    print(compare_three(3, 1, 4))