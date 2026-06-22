def calculate_perimeter(a, b):
    h = ((a - b) ** 2) / ((a + b) ** 2)
    return 3.14159 * (a + b) * (1 + (3 * h) / (10 + (4 - 3 * h) ** 0.5))

if __name__ == '__main__':
    a1, b1 = 3, 4
    perimeter1 = calculate_perimeter(a1, b1)
    print(f"Perimeter for ellipse with semi-major axis {a1} and semi-minor axis {b1}: {perimeter1}")

    a2, b2 = 10, 20
    perimeter2 = calculate_perimeter(a2, b2)
    print(f"Perimeter for ellipse with semi-major axis {a2} and semi-minor axis {b2}: {perimeter2}")