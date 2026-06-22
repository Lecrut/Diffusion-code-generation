import math

def calculate_circle_area(radius):
    if radius < 0:
        return "Error: Radius cannot be negative"
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {'tiny': 0.5, 'medium': 3, 'huge': 10}
    for description, radius in sample_values.items():
        area = calculate_circle_area(radius)
        print(f"The area of a circle with {description} radius ({radius}) is: {area}")