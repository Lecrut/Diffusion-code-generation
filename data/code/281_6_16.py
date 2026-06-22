def sum_of_nine_integers(a, b, c, d, e, f, g, h, i):
    return sum(x for x in (a, b, c, d, e, f, g, h, i))

if __name__ == '__main__':
    result = sum_of_nine_integers(1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(result)