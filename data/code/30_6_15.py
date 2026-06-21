def calculate_circle_area(radius):
    try:
        radius = float(radius)
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return 3.141592653589793 * radius * radius
    except (TypeError, ValueError) as e:
        raise TypeError(f"Invalid input for radius: {e}")

if __name__ == '__main__':
    test_values = [5, 2.5, "10", "abc", -3, 0]
    for value in test_values:
        try:
            result = calculate_circle_area(value)
            print(f"Radius: {value}, Area: {result}")
        except TypeError as e:
            print(f"Radius: {value}, Error: {e}")