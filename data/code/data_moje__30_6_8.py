def calculate_circle_area(radius):
    try:
        radius = float(radius)
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return 3.141592653589793 * radius * radius
    except (TypeError, ValueError):
        return None

if __name__ == '__main__':
    test_values = [5, 2.5, -3, "abc", None, 0]
    for value in test_values:
        result = calculate_circle_area(value)
        print(result)