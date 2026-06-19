import math
PI = math.pi

def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_circle(radius):
    return PI * radius ** 2

def compare_areas(length, width, radius):
    area_rectangle = calculate_area_rectangle(length, width)
    area_circle = calculate_area_circle(radius)
    print(f'Rectangle Area: {area_rectangle:.2f}')
    print(f'Circle Area: {area_circle:.2f}')
if __name__ == '__main__':
    length = 8.0
    width = 3.5
    radius = 4.5
    compare_areas(length, width, radius)