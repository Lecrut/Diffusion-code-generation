def calculate_circle_perimeter(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return 2 * 3.14159 * radius

if __name__ == '__main__':
    sample_radius = 7
    perimeter = calculate_circle_perimeter(sample_radius)
    print(f"The perimeter of a circle with radius {sample_radius} is {perimeter}")