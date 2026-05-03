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
    print("Area Comparison Report")
    print("------------------------")
    print(f"Rectangle Dimensions: Length = {rectangle_length}, Width = {rectangle_width}")
    print(f"Calculated Rectangle Area: {rectangle_area}")
    print("-" * 30)
    print(f"Triangle Dimensions: Base = {triangle_base}, Height = {triangle_height}")
    print(f"Calculated Triangle Area: {triangle_area}")
    if rectangle_area > triangle_area:
        difference = rectangle_area - triangle_area
        print(f"\nComparison: The rectangle area is greater than the triangle area by {difference}")
    elif triangle_area > rectangle_area:
        difference = triangle_area - rectangle_area
        print(f"\nComparison: The triangle area is greater than the rectangle area by {difference}")
    else:
        print("\nComparison: The areas of the rectangle and the triangle are equal.")