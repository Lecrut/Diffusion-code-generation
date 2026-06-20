def reverse_integers(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

if __name__ == '__main__':
    x, y = 10, 20
    reversed_x, reversed_y = reverse_integers(x, y)
    print(reversed_x, reversed_y)