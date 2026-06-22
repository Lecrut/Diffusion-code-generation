import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        'small': 1.0,
        'medium': 5.0,
        'large': 10.0
    }
    
    for description, radius in sample_values.items():
        area = calculate_circle_area(radius)
        print(f"The area of the {description} circle with radius {radius} is {area:.2f}")