import sys
def calculate_area(shape_type, length, width):
    if shape_type == "rectangle":
        return length * width
    elif shape_type == "circle":
        import math
        radius = length
        return math.pi * (radius ** 2)
    else:
        return 0
if __name__ == '__main__':
    shape1_type = "rectangle"
    shape1_length = 10
    shape1_width = 5
    shape2_type = "circle"
    shape2_radius = 3.0
    area1 = calculate_area(shape1_type, shape1_length, shape1_width)
    area2 = calculate_area(shape2_type, shape2_radius, 0)
    print(f"Shape 1 ({shape1_type}) dimensions: Length={shape1_length}, Width={shape1_width}")
    print(f"Area of Shape 1: {area1}")
    print("-" * 30)
    print(f"Shape 2 ({shape2_type}) radius: {shape2_radius}")
    print(f"Area of Shape 2: {area2}")
    if area1 > area2:
        print("\nComparison Result:")
        print("Shape 1 has the greater area.")
    elif area2 > area1:
        print("\nComparison Result:")
        print("Shape 2 has the greater area.")
    else:
        print("\nComparison Result:")
        print("Both shapes have equal areas.")