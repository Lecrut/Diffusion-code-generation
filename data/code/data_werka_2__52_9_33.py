import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_radii = [4, 9, 12]
    for index, radius in enumerate(sample_radii, start=1):
        try:
            computed_area = calculate_circle_area(radius)
            print(f"Sample {index}: The area of a circle with radius {radius} is {computed_area:.2f}")
        except ValueError as e:
            print(e)