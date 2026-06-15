import math
def calculate_rectangle_area(length, width):
    return length * width
def calculate_triangle_area(base, height):
    return 0.5 * base * height
if __name__ == '__main__':
    rectangle_length = 10
    rectangle_width = 5
    triangle_base = 8
    triangle_height = 6
    rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
    triangle_area = calculate_triangle_area(triangle_base, triangle_height)
    print("--- Shape Area Comparison ---")
    print("Rectangle Dimensions: Length =", rectangle_length, ", Width =", rectangle_width)
    print("Calculated Rectangle Area:", rectangle_area)
    print("\nTriangle Dimensions: Base =", triangle_base, ", Height =", triangle_height)
    print("Calculated Triangle Area:", triangle_area)
    if rectangle_area > triangle_area:
        difference = rectangle_area - triangle_area
        print("\nThe Rectangle has a larger area by:", difference)
    elif triangle_area > rectangle_area:
        difference = triangle_area - rectangle_area
        print("\nThe Triangle has a larger area by:", difference)
    else:
        print("\nThe areas of the rectangle and the triangle are equal.")