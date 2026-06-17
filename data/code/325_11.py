def compare_quantities(a, b):
    if a < b:
        return (a, b)
    elif b < a:
        return (b, a)
    else:
        return (a, b)
if __name__ == '__main__':
    print(compare_quantities(5, 10))
    print(compare_quantities(20, 3))
    print(compare_quantities(7, 7))
    print(compare_quantities(-1, -5))