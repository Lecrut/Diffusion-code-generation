import math

def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_circle(radius):
    return math.pi * radius ** 2

def compare_areas(rectangle_length, rectangle_width, circle_radius):
    area_rectangle = calculate_area_rectangle(rectangle_length, rectangle_width)
    area_circle = calculate_area_circle(circle_radius)
    
    print(f"Rectangle Area: {area_rectangle:.2f}")
    print(f"Circle Area: {area_circle:.2f}")

if __name__ == '__main__':
    compare_areas(5, 3, 4)