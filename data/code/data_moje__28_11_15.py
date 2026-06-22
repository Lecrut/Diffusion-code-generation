def sort_descending(a, b):
    if a >= b:
        return (a, b)
    else:
        return (b, a)
if __name__ == '__main__':
    print(sort_descending(3.14, 2.71))
    print(sort_descending(10, 10))
    print(sort_descending(-5, -2))
    print(sort_descending(0, 100))
    print(sort_descending(10000000000.0, 1e-10))