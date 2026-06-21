def sort_descending(a, b):
    if a >= b:
        return [a, b]
    return [b, a]

if __name__ == '__main__':
    x = 5
    y = 10
    print(sort_descending(x, y))