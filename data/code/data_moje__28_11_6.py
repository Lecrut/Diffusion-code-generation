def sort_descending(a, b):
    if a > b:
        return a, b
    else:
        return b, a

if __name__ == '__main__':
    x = 10
    y = 5
    print(sort_descending(x, y))
    print(sort_descending(3, 8))
    print(sort_descending(-1, -5))
    print(sort_descending(0, 0))