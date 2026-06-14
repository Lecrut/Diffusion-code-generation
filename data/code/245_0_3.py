import math
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)
def calculate_rectangle_area(length, width):
    return length * width
if __name__ == '__main__':
    circle_radius = 5.0
    rectangle_length = 4.0
    rectangle_width = 6.0
    circle_area = calculate_circle_area(circle_radius)
    rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
    print(f"Area of the circle: {circle_area}")
    print(f"Area of the rectangle: {rectangle_area}")
    if circle_area == rectangle_area:
        print("The areas of the two shapes are equal.")
    else:
        print("The areas of the two shapes are not equal.")