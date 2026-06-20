def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

if __name__ == '__main__':
    x, y = 7, 14
    x, y = swap(x, y)
    print(f"Swapped values: x={x}, y={y}")