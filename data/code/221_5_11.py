def sort_three_numbers(a, b, c):
    if a <= b:
        if b <= c:
            return a, b, c
        elif a <= c:
            return a, c, b
        else:
            return c, a, b
    else:
        if a <= c:
            return b, a, c
        elif b <= c:
            return b, c, a
        else:
            return c, b, a

if __name__ == '__main__':
    print(sort_three_numbers(5, 1, 3))