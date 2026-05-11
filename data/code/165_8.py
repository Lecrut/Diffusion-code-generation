import math
def calculate_area_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    area = math.pi * (radius ** 2)
    return area
def calculate_circumference_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    circumference = 2 * math.pi * radius
    return circumference
def main():
    print("--- Circle Calculation Examples ---")
    sample_radius_1 = 5.0
    sample_radius_2 = 10.5
    try:
        area_1 = calculate_area_circle(sample_radius_1)
        print(f"Radius: {sample_radius_1}")
        print(f"Area: {area_1:.4f}")
    except ValueError as e:
        print(f"Error calculating area for radius {sample_radius_1}: {e}")
    print("-" * 30)
    try:
        circumference_2 = calculate_circumference_circle(sample_radius_2)
        print(f"Radius: {sample_radius_2}")
        print(f"Circumference: {circumference_2:.4f}")
    except ValueError as e:
        print(f"Error calculating circumference for radius {sample_radius_2}: {e}")
    print("-" * 30)
    invalid_radius = -2.0
    print(f"Testing invalid radius: {invalid_radius}")
    try:
        calculate_area_circle(invalid_radius)
    except ValueError as e:
        print(f"Caught expected error: {e}")
if __name__ == '__main__':
    main()