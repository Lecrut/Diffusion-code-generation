import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_categories = {
        'tiny': 0.5,
        'small': 1.0,
        'medium': 3.0,
        'large': 6.0
    }
    
    for category, radius in sample_categories.items():
        try:
            area = calculate_circle_area(radius)
            print(f"The area of a {category} circle with radius {radius} is: {area:.2f}")
        except ValueError as e:
            print(e)