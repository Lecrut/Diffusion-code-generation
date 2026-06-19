import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_values = {'radius': 3}
    area = calculate_circle_area(sample_values['radius'])
    print(f"The area of the circle with radius {sample_values['radius']} is: {area}")