import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    try:
        sample_values = [1, 5, 10, -3, 'a']
        for value in sample_values:
            area = calculate_circle_area(value)
            print(f"The area of a circle with radius {value} is: {area}")
    except (TypeError, ValueError) as e:
        print(e)