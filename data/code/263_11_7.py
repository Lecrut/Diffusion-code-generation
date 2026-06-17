def compare_three(a, b, c):
    if a <= b and b <= c:
        return (a, b, c)
    elif a <= c and c <= b:
        return (a, c, b)
    elif b <= a and a <= c:
        return (b, a, c)
    elif b <= c and c <= a:
        return (b, c, a)
    elif a <= b and b <= c:
        return (a, b, c)
    else:
        if a <= b:
            if b <= c:
                return (a, b, c)
            else:
                if a <= c:
                    return (a, c, b)
                else:
                    return (c, a, b)
        else:
            if b <= a:
                if a <= c:
                    return (b, a, c)
                else:
                    if b <= c:
                        return (b, c, a)
                    else:
                        return (c, b, a)
            else:
                if c <= a:
                    return (c, a, b)
                else:
                    return (a, b, c)
def compare_three(a, b, c):
    numbers = sorted([a, b, c])
    return tuple(numbers)
if __name__ == '__main__':
    print(compare_three(5, 2, 8))
    print(compare_three(10, 4, 7))
    print(compare_three(3, 3, 3))
    print(compare_three(1, 9, 5))
    print(compare_three(100, 200, 50))