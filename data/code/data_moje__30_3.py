def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 3.141592653589793 * radius * radius

if __name__ == '__main__':
    test_radius_1 = 5
    test_radius_2 = 10.5
    test_radius_3 = -3
    print(calculate_circle_area(test_radius_1))
    print(calculate_circle_area(test_radius_2))
    try:
        print(calculate_circle_area(test_radius_3))
    except ValueError as e:
        print(f"Error: {e}")