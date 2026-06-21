def sort_descending(a, b):
    if a > b:
        return [a, b]
    else:
        return [b, a]

if __name__ == '__main__':
    x = 42
    y = 17
    print(sort_descending(x, y))