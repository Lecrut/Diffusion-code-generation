def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius must be non-negative.")
    return 3.14159265359 * radius * radius

if __name__ == '__main__':
    sample_radius = 5
    area = calculate_circle_area(sample_radius)
    print(area)
    negative_radius = -3
    try:
        calculate_circle_area(negative_radius)
    except ValueError as e:
        print(e)