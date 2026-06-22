import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    try:
        sample_values = {'tiny': 0.5, 'normal': 3, 'giant': 10}
        for size, radius in sample_values.items():
            area = calculate_circle_area(radius)
            print(f"The area of a {size} circle with radius {radius} is: {area}")
    except (TypeError, ValueError) as e:
        print(e)