def swap_values(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")
    return b, a

if __name__ == '__main__':
    x, y = 3, 7
    swapped_x, swapped_y = swap_values(x, y)
    print(f"Swapped values: x={swapped_x}, y={swapped_y}")