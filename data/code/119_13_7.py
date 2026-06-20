def swap_values(a, b):
    return b, a

if __name__ == '__main__':
    x, y = 8, 15
    swapped_x, swapped_y = swap_values(x, y)
    print(f"After swap: x={swapped_x}, y={swapped_y}")