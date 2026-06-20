def reverse_integers(a, b):
    a, b = b, a
    return a, b

if __name__ == '__main__':
    x, y = 5, 10
    reversed_x, reversed_y = reverse_integers(x, y)
    print(reversed_x, reversed_y)