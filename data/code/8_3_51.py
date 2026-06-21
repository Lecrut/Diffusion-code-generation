import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius_values = {'small': 1, 'medium': 3.5, 'large': 7}
    for size, radius in sample_radius_values.items():
        area = calculate_circle_area(radius)
        print(f"The area of a circle with {size} radius ({radius}) is: {area}")