def compare_three(a, b, c):
    if a <= b <= c:
        return (a, b, c)
    elif a <= c <= b:
        return (a, c, b)
    elif b <= a <= c:
        return (b, a, c)
    elif b <= c <= a:
        return (b, c, a)
    elif c <= a <= b:
        return (c, a, b)
    elif c <= b <= a:
        return (c, b, a)
    else:
        return (b, a, c)
if __name__ == '__main__':
    print(compare_three(1, 5, 3))
    print(compare_three(10, 2, 8))
    print(compare_three(4, 4, 4))
    print(compare_three(7, 1, 9))
    print(compare_three(5, 8, 3))
    print(compare_three(9, 3, 7))