def swap_values(x, y):
    temp = x
    x = y
    y = temp
    return x, y

if __name__ == '__main__':
    a, b = 3, 8
    a, b = swap_values(a, b)
    print(f"Swapped values: a={a}, b={b}")