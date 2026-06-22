import math

def calculate_circle_area(radius):
    return math.pi * radius**2

if __name__ == '__main__':
    sample_values = {
        'small': 1,
        'medium': 5,
        'large': 10,
        'tiny': 0.1
    }
    
    for description, radius in sample_values.items():
        area = calculate_circle_area(radius)
        print(f"Area of circle with {description} radius ({radius}): {area}")