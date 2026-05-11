import math
def calculate_area_of_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * (radius ** 2)
    return area
def calculate_circumference_of_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    circumference = 2 * math.pi * radius
    return circumference
def main():
    print("--- Circle Calculation Script ---")
    sample_radius_1 = 5.0
    sample_radius_2 = 10.5
    print(f"\nCalculating for Radius 1: {sample_radius_1}")
    try:
        area1 = calculate_area_of_circle(sample_radius_1)
        circumference1 = calculate_circumference_of_circle(sample_radius_1)
        print(f"Area of circle with radius {sample_radius_1}: {area1:.4f}")
        print(f"Circumference of circle with radius {sample_radius_1}: {circumference1:.4f}")
    except ValueError as e:
        print(f"Error calculating for radius {sample_radius_1}: {e}")
    print("\n" + "=" * 30)
    print(f"Calculating for Radius 2: {sample_radius_2}")
    try:
        area2 = calculate_area_of_circle(sample_radius_2)
        circumference2 = calculate_circumference_of_circle(sample_radius_2)
        print(f"Area of circle with radius {sample_radius_2}: {area2:.4f}")
        print(f"Circumference of circle with radius {sample_radius_2}: {circumference2:.4f}")
    except ValueError as e:
        print(f"Error calculating for radius {sample_radius_2}: {e}")
if __name__ == '__main__':
    main()