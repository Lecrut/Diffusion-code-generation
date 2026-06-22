def sort_three_numbers(a, b, c):
    if a < b:
        if a < c:
            if b < c:
                return (a, b, c)
            else:
                return (a, c, b)
        else:
            return (c, a, b)
    elif b < c:
        if a < c:
            return (b, a, c)
        else:
            return (b, c, a)
    else:
        return (c, b, a)
if __name__ == '__main__':
    x, y, z = sort_three_numbers(5, 1, 3)
    print(x, y, z)