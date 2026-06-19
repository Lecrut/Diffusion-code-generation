import math

def calculate_circle_area(radius):
    if radius < 0:
        return None
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 5
    area = calculate_circle_area(sample_radius)
    if area is not None:
        print(f"The area of a circle with radius {sample_radius} is: {area}")
    else:
        print("Invalid radius provided.")