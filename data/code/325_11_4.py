def compare_quantities(a, b):
    if a < b:
        return (a, b)
    else:
        return (b, a)
if __name__ == '__main__':
    print(compare_quantities(5, 10))
    print(compare_quantities(10, 5))
    print(compare_quantities(3.14, 2.71))
    print(compare_quantities(100, 100))