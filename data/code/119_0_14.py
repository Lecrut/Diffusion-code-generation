def swap(a, b):
    return (b, a)

if __name__ == '__main__':
    x, y = 5, 10
    print(f"Before swap: x={x}, y={y}")
    x, y = swap(x, y)
    print(f"After swap: x={x}, y={y}")