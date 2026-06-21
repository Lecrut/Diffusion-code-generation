import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_values = {
        'small': 1.5,
        'medium': 3.0,
        'large': 4.5
    }
    
    for size, radius in sample_values.items():
        area = calculate_circle_area(radius)
        print(f"The area of a circle with {size} radius ({radius}) is: {area}")