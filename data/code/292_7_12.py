def calculate_ellipse_perimeter(a, b):
    h = ((a - b) ** 2) / ((a + b) ** 2)
    return (a + b) * (1 + (3 * h) / (10 + (4 - 3 * h) ** 0.5))

if __name__ == '__main__':
    print(calculate_ellipse_perimeter(5, 3))