import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def compare_and_print_areas(length, width, radius):
    rectangle_area = calculate_rectangle_area(length, width)
    circle_area = calculate_circle_area(radius)
    print(f"Rectangle Area: {rectangle_area:.2f}")
    print(f"Circle Area: {circle_area:.2f}")

if __name__ == '__main__':
    length = 8.0
    width = 4.5
    radius = 6.0
    compare_and_print_areas(length, width, radius)