def calculate_circumference(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return 2 * 3.14159 * radius

if __name__ == '__main__':
    sample_radius = 7
    try:
        result = calculate_circumference(sample_radius)
        print(f"Circumference for radius {sample_radius}: {result}")
    except ValueError as e:
        print(f"Error: {e}")