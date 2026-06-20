def swap(a, b):
    a, b = b, a
    return a, b

if __name__ == '__main__':
    x, y = 5, 10
    print(swap(x, y))