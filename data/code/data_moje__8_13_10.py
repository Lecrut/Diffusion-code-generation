import math

def calculate_scaled_rectangle_area(base, height, scale_factor):
    return (base * scale_factor) * (height * scale_factor)

def calculate_scaled_circle_area(radius, scale_factor):
    return math.pi * (radius * scale_factor) ** 2

if __name__ == '__main__':
    rectangle_area = calculate_scaled_rectangle_area(10, 5, 2)
    circle_area = calculate_scaled_circle_area(7, 1.5)
    print(rectangle_area)
    print(circle_area)