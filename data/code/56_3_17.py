import math

def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_circle(radius):
    return math.pi * radius ** 2

def compare_areas(length, width, radius):
    area_rectangle = calculate_area_rectangle(length, width)
    area_circle = calculate_area_circle(radius)
    return f"Rectangle Area: {area_rectangle:.2f}, Circle Area: {area_circle:.2f}"

if __name__ == '__main__':
    length = 5.0
    width = 3.0
    radius = 4.0
    print(compare_areas(length, width, radius))