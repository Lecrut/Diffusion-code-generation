def swap_values(a, b):
    values = [a, b]
    values[0], values[1] = values[1], values[0]
    return values

if __name__ == '__main__':
    num1 = 7
    num2 = 3
    swapped = swap_values(num1, num2)
    print(swapped)