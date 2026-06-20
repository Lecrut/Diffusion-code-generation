def reverse_integers(a, b):
    temp = a
    a = b
    b = temp
    return a, b

if __name__ == '__main__':
    x = 30
    y = 40
    reversed_x, reversed_y = reverse_integers(x, y)
    print(f"Reversed values: x={reversed_x}, y={reversed_y}")