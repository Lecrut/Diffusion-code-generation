def swap_values(a, b):
    values = [a, b]
    values[0], values[1] = values[1], values[0]
    return values

if __name__ == '__main__':
    x, y = 8, 3
    swapped = swap_values(x, y)
    print(swapped)