def reverse_integers(a, b):
    a, b = b, a
    return a, b

if __name__ == '__main__':
    x, y = 5, 10
    x, y = reverse_integers(x, y)
    print(f"Reversed values: x={x}, y={y}")