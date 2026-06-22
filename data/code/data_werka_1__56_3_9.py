import math

def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_circle(radius):
    return math.pi * radius ** 2

def compare_areas(length, width, radius):
    rectangle_area = calculate_area_rectangle(length, width)
    circle_area = calculate_area_circle(radius)
    print(f"Rectangle Area: {rectangle_area:.2f}")
    print(f"Circle Area: {circle_area:.2f}")

if __name__ == '__main__':
    length = 8.0
    width = 4.5
    radius = 6.0
    compare_areas(length, width, radius)