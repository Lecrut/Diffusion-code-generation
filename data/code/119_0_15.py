def swap(a, b):
    a, b = b, a
    return a, b

if __name__ == '__main__':
    x, y = 3, 7
    x, y = swap(x, y)
    print(f"x: {x}, y: {y}")