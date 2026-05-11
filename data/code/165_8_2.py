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
    print("--- Circle Calculation Demonstration ---")
    sample_radius = 5.0
    print(f"Input Radius: {sample_radius}")
    try:
        area = calculate_area_of_circle(sample_radius)
        print(f"Area of the circle: {area:.4f}")
        circumference = calculate_circumference_of_circle(sample_radius)
        print(f"Circumference of the circle: {circumference:.4f}")
    except ValueError as e:
        print(f"Error during calculation: {e}")
if __name__ == '__main__':
    main()