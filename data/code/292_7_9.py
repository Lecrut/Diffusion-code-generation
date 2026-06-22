def validate_ellipse_parameters(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Ellipse parameters must be positive numbers")

def calculate_perimeter(a, b):
    validate_ellipse_parameters(a, b)
    return 2 * (a + b) * (1 + (3 * ((a - b)**2 / ((a + b)**2)))**(1/3)) / (1 + (3 * ((a + b)**2 / ((a - b)**2)))**(1/3))

if __name__ == '__main__':
    a1, b1 = 5, 3
    perimeter1 = calculate_perimeter(a1, b1)
    print(f"Perimeter for ellipse with semi-major axis {a1} and semi-minor axis {b1}: {perimeter1:.2f}")

    a2, b2 = 10, 6
    perimeter2 = calculate_perimeter(a2, b2)
    print(f"Perimeter for ellipse with semi-major axis {a2} and semi-minor axis {b2}: {perimeter2:.2f}")