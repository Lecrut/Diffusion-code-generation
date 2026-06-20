def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b

if __name__ == '__main__':
    x = 15
    y = 25
    swapped_x, swapped_y = swap_numbers(x, y)
    print(f"Swapped values: x={swapped_x}, y={swapped_y}")