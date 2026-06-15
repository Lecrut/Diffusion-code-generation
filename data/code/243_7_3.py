def calculate_circumference(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive value.")
    return 2 * 3.14159 * radius
if __name__ == '__main__':
    valid_radius = 5
    invalid_radius_zero = 0
    invalid_radius_negative = -2
    try:
        circumference_valid = calculate_circumference(valid_radius)
        print(f"Circumference for radius {valid_radius}: {circumference_valid}")
    except ValueError as e:
        print(f"Error calculating circumference for {valid_radius}: {e}")
    try:
        calculate_circumference(invalid_radius_zero)
    except ValueError as e:
        print(f"Error calculating circumference for {invalid_radius_zero}: {e}")
    try:
        calculate_circumference(invalid_radius_negative)
    except ValueError as e:
        print(f"Error calculating circumference for {invalid_radius_negative}: {e}")