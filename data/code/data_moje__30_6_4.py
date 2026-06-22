def calculate_circle_area(radius):
    try:
        r = float(radius)
        if r < 0:
            raise ValueError("Radius cannot be negative")
        return 3.141592653589793 * r * r
    except (TypeError, ValueError):
        return None

if __name__ == '__main__':
    print(calculate_circle_area(5))
    print(calculate_circle_area(2.5))
    print(calculate_circle_area("invalid"))
    print(calculate_circle_area(-3))