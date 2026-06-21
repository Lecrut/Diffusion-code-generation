def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 3.14159265359 * radius * radius

if __name__ == '__main__':
    test_radius_1 = 5
    test_radius_2 = 0
    test_radius_3 = 2.5
    print(calculate_circle_area(test_radius_1))
    print(calculate_circle_area(test_radius_2))
    print(calculate_circle_area(test_radius_3))