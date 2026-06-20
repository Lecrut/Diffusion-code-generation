def reverse_integers(a, b):
    a, b = b, a
    return a, b

if __name__ == '__main__':
    x, y = reverse_integers(5, 10)
    print(f"Reversed values: {x}, {y}")