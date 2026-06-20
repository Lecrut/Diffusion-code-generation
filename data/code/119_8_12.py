def swap_integers(a, b):
    temp = a
    a = b
    b = temp
    return a, b

if __name__ == '__main__':
    x, y = 5, 10
    x, y = swap_integers(x, y)
    print(f"Swapped values: x={x}, y={y}")