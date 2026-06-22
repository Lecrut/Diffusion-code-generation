import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = [1, 2, 0, 10, 5.5]
    for value in sample_values:
        try:
            area = calculate_circle_area(value)
            print(f"Radius: {value}, Area: {area}")
        except ValueError as e:
            print(e)