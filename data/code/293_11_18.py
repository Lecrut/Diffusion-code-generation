import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def convert_to_imperial(area_metric):
    return area_metric * 0.000645359

if __name__ == '__main__':
    circle_radius = 5
    rectangle_length = 10
    rectangle_width = 7
    triangle_base = 8
    triangle_height = 6

    circle_area_metric = calculate_circle_area(circle_radius)
    rectangle_area_metric = calculate_rectangle_area(rectangle_length, rectangle_width)
    triangle_area_metric = calculate_triangle_area(triangle_base, triangle_height)

    circle_area_imperial = convert_to_imperial(circle_area_metric)
    rectangle_area_imperial = convert_to_imperial(rectangle_area_metric)
    triangle_area_imperial = convert_to_imperial(triangle_area_metric)

    print(f"Circle area (metric): {circle_area_metric} m^2")
    print(f"Rectangle area (metric): {rectangle_area_metric} m^2")
    print(f"Triangle area (metric): {triangle_area_metric} m^2")

    print(f"Circle area (imperial): {circle_area_imperial} sq ft")
    print(f"Rectangle area (imperial): {rectangle_area_imperial} sq ft")
    print(f"Triangle area (imperial): {triangle_area_imperial} sq ft")