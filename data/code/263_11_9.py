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
    print(compare_three(1, 5, 3))
    print(compare_three(10, 2, 8))
    print(compare_three(4, 4, 4))
    print(compare_three(7, 1, 9))
    print(compare_three(100, 50, 25))