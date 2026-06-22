def sort_descending(a, b):
    if a > b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    print(sort_descending(10, 5))
    print(sort_descending(3, 7))
    print(sort_descending(4.5, 4.5))
    print(sort_descending(-1, -2))