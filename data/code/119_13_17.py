def swap_values(a, b):
    return b, a

if __name__ == '__main__':
    values = {10: 20, 5: 10}
    x, y = values[10], values[5]
    swapped_x, swapped_y = swap_values(x, y)
    print(f"Swapped values: x={swapped_x}, y={swapped_y}")