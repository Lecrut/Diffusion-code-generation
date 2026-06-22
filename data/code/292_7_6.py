def calculate_perimeter(a, b):
    return 2 * (a + b) * (1 + (3 * ((a - b) / (a + b)) ** 2) / (10 + sqrt(4 - 3 * ((a - b) / (a + b)) ** 2)))

if __name__ == '__main__':
    ellipse1 = (5, 3)
    perimeter1 = calculate_perimeter(*ellipse1)
    print(f"Perimeter for ellipse with semi-major axis {ellipse1[0]} and semi-minor axis {ellipse1[1]}: {perimeter1}")

    ellipse2 = (10, 7)
    perimeter2 = calculate_perimeter(*ellipse2)
    print(f"Perimeter for ellipse with semi-major axis {ellipse2[0]} and semi-minor axis {ellipse2[1]}: {perimeter2}")