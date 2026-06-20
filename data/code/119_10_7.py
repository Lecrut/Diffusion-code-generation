def swap_values(a, b):
    return (b, a)

if __name__ == '__main__':
    x, y = 5, 10
    x, y = swap_values(x, y)
    print(f"Swapped values: x={x}, y={y}")