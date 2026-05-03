import math
def calculate_circle_properties(radius):
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    return area, perimeter
def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
if __name__ == '__main__':
    circle_radius = 5.0
    rectangle_length = 10.0
    rectangle_width = 4.0
    circle_area, circle_perimeter = calculate_circle_properties(circle_radius)
    rectangle_area, rectangle_perimeter = calculate_rectangle_properties(rectangle_length, rectangle_width)
    print(f"Circle:")
    print(f"Radius: {circle_radius}")
    print(f"Area: {circle_area}")
    print(f"Perimeter (Circumference): {circle_perimeter}")
    print("\nRectangle:")
    print(f"Length: {rectangle_length}")
    print(f"Width: {rectangle_width}")
    print(f"Area: {rectangle_area}")
    print(f"Perimeter: {rectangle_perimeter}")