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
    print("\n--- Calculation for Radius 1: %.2f ---" % sample_radius_1)
    try:
        area1 = calculate_area_of_circle(sample_radius_1)
        circumference1 = calculate_circumference_of_circle(sample_radius_1)
        print("Area:", area1)
        print("Circumference:", circumference1)
    except ValueError as e:
        print("Error:", e)
    print("\n--- Calculation for Radius 2: %.2f ---" % sample_radius_2)
    try:
        area2 = calculate_area_of_circle(sample_radius_2)
        circumference2 = calculate_circumference_of_circle(sample_radius_2)
        print("Area:", area2)
        print("Circumference:", circumference2)
    except ValueError as e:
        print("Error:", e)
if __name__ == '__main__':
    main()