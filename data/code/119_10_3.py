def swap_values(a, b):
    temp = a
    a = b
    b = temp
    return a, b

if __name__ == '__main__':
    x, y = 7, 3
    x, y = swap_values(x, y)
    print(f"Swapped values: x={x}, y={y}")