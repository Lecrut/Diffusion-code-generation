def calculate_circle_area(radius):
    try:
        numeric_radius = float(radius)
        if numeric_radius < 0:
            raise ValueError("Radius cannot be negative")
        return 3.14159 * numeric_radius * numeric_radius
    except (TypeError, ValueError):
        return "Error: Invalid input for radius"

if __name__ == '__main__':
    print(calculate_circle_area(5))
    print(calculate_circle_area(2.5))
    print(calculate_circle_area("abc"))
    print(calculate_circle_area(-1))
    print(calculate_circle_area(None))