import math
if __name__ == '__main__':
    circle_radius = 5.0
    rectangle_length = 10.0
    rectangle_width = 4.0
    circle_area = math.pi * circle_radius**2
    circle_perimeter = 2 * math.pi * circle_radius
    rectangle_area = rectangle_length * rectangle_width
    rectangle_perimeter = 2 * (rectangle_length + rectangle_width)
    print(f"Circle:")
    print(f"Radius: {circle_radius}")
    print(f"Area: {circle_area}")
    print(f"Perimeter (Circumference): {circle_perimeter}")
    print("\nRectangle:")
    print(f"Length: {rectangle_length}")
    print(f"Width: {rectangle_width}")
    print(f"Area: {rectangle_area}")
    print(f"Perimeter: {rectangle_perimeter}")