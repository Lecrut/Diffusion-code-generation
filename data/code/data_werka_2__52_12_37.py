import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {
        "small": 3.0,
        "medium": 5.0,
        "large": 7.5
    }
    
    for size, radius in sample_values.items():
        try:
            area = calculate_circle_area(radius)
            print(f"The area of a {size} circle with radius {radius} is {area:.2f}")
        except ValueError as e:
            print(e)