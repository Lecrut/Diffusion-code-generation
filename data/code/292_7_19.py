from math import pi

def calculate_perimeter(a, b):
    return pi * (3 * (a + b) - ((a - b) ** 2) / ((a + b) ** 2))

if __name__ == '__main__':
    a1, b1 = 3, 4
    perimeter1 = calculate_perimeter(a1, b1)
    print(f"Perimeter for ellipse with semi-major axis {a1} and semi-minor axis {b1}: {perimeter1:.2f}")

    a2, b2 = 5, 7
    perimeter2 = calculate_perimeter(a2, b2)
    print(f"Perimeter for ellipse with semi-major axis {a2} and semi-minor axis {b2}: {perimeter2:.2f}")