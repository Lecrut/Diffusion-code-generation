def calculate_circle_area(radius):
    try:
        numeric_radius = float(radius)
        if numeric_radius < 0:
            raise ValueError("Radius cannot be negative")
        return 3.141592653589793 * numeric_radius * numeric_radius
    except (TypeError, ValueError) as e:
        raise TypeError(f"Invalid radius value: {e}")

if __name__ == '__main__':
    print(calculate_circle_area(5))
    print(calculate_circle_area(2.5))
    try:
        print(calculate_circle_area("abc"))
    except TypeError as e:
        print(e)
    try:
        print(calculate_circle_area(-10))
    except TypeError as e:
        print(e)