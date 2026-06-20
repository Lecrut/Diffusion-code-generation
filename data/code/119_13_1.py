def swap_values(a, b):
    a, b = b, a
    return a, b

if __name__ == '__main__':
    x, y = 5, 10
    swapped_x, swapped_y = swap_values(x, y)
    print(swapped_x, swapped_y)