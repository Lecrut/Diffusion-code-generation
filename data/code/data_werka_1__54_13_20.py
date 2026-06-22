import math

def calculate_circle_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_values = {
        "small": 1.0,
        "medium": 5.0,
        "large": 10.0
    }
    
    for size, radius in sample_values.items():
        try:
            area = calculate_circle_area(radius)
            print(f"The area of a circle with {size} radius ({radius}) is: {area}")
        except ValueError as e:
            print(e)