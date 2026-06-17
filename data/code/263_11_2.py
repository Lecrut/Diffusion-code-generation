def compare_three(a, b, c):
    if a < b:
        if b < c:
            return (a, b, c)
        else:
            if a < c:
                return (a, c, b)
            else:
                return (c, a, b)
    else:
        if b < c:
            if a < b:
                return (a, b, c)
            else:
                if a < c:
                    return (b, a, c)
                else:
                    return (b, c, a)
        else:
            if a < c:
                return (b, a, c)
            else:
                return (c, a, b)
if __name__ == '__main__':
    print(compare_three(5, 2, 8))
    print(compare_three(10, 4, 7))
    print(compare_three(3, 1, 2))
    print(compare_three(1, 1, 1))
    print(compare_three(9, 6, 3))