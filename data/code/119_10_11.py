def swap_values(a, b):
    return (b, a)

if __name__ == '__main__':
    values = {1: 5, 2: 10}
    x, y = values[1], values[2]
    x, y = swap_values(x, y)
    print(f"Swapped values: x={x}, y={y}")