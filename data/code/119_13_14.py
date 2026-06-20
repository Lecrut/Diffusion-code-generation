def swap_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers")
    return b, a

if __name__ == '__main__':
    x, y = 42, 99
    print(f"Before swap: x={x}, y={y}")
    swapped_x, swapped_y = swap_numbers(x, y)
    print(f"After swap: x={swapped_x}, y={swapped_y}")