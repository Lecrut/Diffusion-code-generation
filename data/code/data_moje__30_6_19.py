def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.141592653589793 * (radius ** 2)

if __name__ == '__main__':
    r1 = 5
    result1 = calculate_circle_area(r1)
    print(f"Area of circle with radius {r1}: {result1}")

    r2 = 10
    result2 = calculate_circle_area(r2)
    print(f"Area of circle with radius {r2}: {result2}")

    try:
        calculate_circle_area("5")
    except TypeError as e:
        print(f"Caught TypeError for non-numeric input: {e}")