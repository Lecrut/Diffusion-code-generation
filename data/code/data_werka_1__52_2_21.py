import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        'small': 3,
        'medium': 7.5,
        'large': 10
    }
    for name, radius in sample_values.items():
        try:
            area = calculate_circle_area(radius)
            print(f"The area of the {name} circle with radius {radius} is {area:.2f}")
        except ValueError as e:
            print(e)