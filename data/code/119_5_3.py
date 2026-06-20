def swap_values(a, b):
    values = [a, b]
    values[0], values[1] = values[1], values[0]
    return values[0], values[1]

if __name__ == '__main__':
    x, y = 5, 10
    swapped_x, swapped_y = swap_values(x, y)
    print(f"Swapped values: x={swapped_x}, y={swapped_y}")