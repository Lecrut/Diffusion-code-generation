import math

def calculate_perimeter(width, height):
    return 2 * (width + height)

def calculate_area(width, height):
    return width * height

if __name__ == '__main__':
    width_val = 5.0
    height_val = 3.0
    perimeter_result = calculate_perimeter(width_val, height_val)
    area_result = calculate_area(width_val, height_val)
    print(f"Perimeter: {perimeter_result}")
    print(f"Area: {area_result}")