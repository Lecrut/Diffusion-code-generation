import math

def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

if __name__ == '__main__':
    sample_radius = 7
    calculated_area = calculate_circle_area(sample_radius)
    print(f"The area of a circle with radius {sample_radius} is: {calculated_area}")