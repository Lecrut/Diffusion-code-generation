import math
def calculate_areas(length, width, radius):
    rectangle_area = length * width
    circle_area = math.pi * (radius ** 2)
    return rectangle_area, circle_area
if __name__ == '__main__':
    rectangle_length = 10.0
    rectangle_width = 5.0
    circle_radius = 4.0
    rect_area, circ_area = calculate_areas(rectangle_length, rectangle_width, circle_radius)
    print(f"Rectangle Length: {rectangle_length}")
    print(f"Rectangle Width: {rectangle_width}")
    print(f"Circle Radius: {circle_radius}")
    print("-" * 30)
    print(f"Area of Rectangle: {rect_area}")
    print(f"Area of Circle: {circ_area}")
    if rect_area > circ_area:
        print("The rectangle has a larger area.")
    elif circ_area > rect_area:
        print("The circle has a larger area.")
    else:
        print("The areas of the rectangle and the circle are equal.")