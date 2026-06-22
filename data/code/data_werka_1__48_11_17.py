import math

def calculate_perimeter(width, height):
    return 2 * (width + height)

def calculate_area(width, height):
    return width * height

if __name__ == '__main__':
    sample_width = 7.0
    sample_height = 4.5
    perimeter_result = calculate_perimeter(sample_width, sample_height)
    area_result = calculate_area(sample_width, sample_height)
    print(f"Perimeter: {perimeter_result}")
    print(f"Area: {area_result}")