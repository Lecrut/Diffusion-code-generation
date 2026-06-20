def swap_values(x, y):
    temp = x
    x = y
    y = temp
    return (x, y)

if __name__ == '__main__':
    value1 = 42
    value2 = 99
    swapped_values = swap_values(value1, value2)
    print(swapped_values)