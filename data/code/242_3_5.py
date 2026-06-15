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
    print("Rectangle Dimensions:")
    print(f"Length: {rectangle_length}")
    print(f"Width: {rectangle_width}")
    print(f"Calculated Area: {rectangle_area}")
    print("\nTriangle Dimensions:")
    print(f"Base: {triangle_base}")
    print(f"Height: {triangle_height}")
    print(f"Calculated Area: {triangle_area}")
    if rectangle_area > triangle_area:
        difference = rectangle_area - triangle_area
        print("\nComparison:")
        print(f"The rectangle area ({rectangle_area}) is greater than the triangle area ({triangle_area}) by {difference}.")
    elif triangle_area > rectangle_area:
        difference = triangle_area - rectangle_area
        print("\nComparison:")
        print(f"The triangle area ({triangle_area}) is greater than the rectangle area ({rectangle_area}) by {difference}.")
    else:
        print("\nComparison:")
        print("The areas of the rectangle and the triangle are equal.")