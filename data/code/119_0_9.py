def swap(a, b):
    return (b, a)

if __name__ == '__main__':
    x, y = 15, 20
    x, y = swap(x, y)
    print(f"x: {x}, y: {y}")