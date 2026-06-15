import sys
def calculate_area(shape_type, length, width):
    if shape_type == "rectangle":
        return length * width
    elif shape_type == "circle":
        import math
        radius = length / 2
        return math.pi * (radius ** 2)
    else:
        return 0
if __name__ == '__main__':
    shape1_type = "rectangle"
    shape1_length = 10
    shape1_width = 5
    shape2_type = "circle"
    shape2_radius = 3.5
    area1 = calculate_area(shape1_type, shape1_length, shape1_width)
    area2 = calculate_area(shape2_type, shape2_radius, 0)
    print(f"Shape 1 ({shape1_type}): Area = {area1}")
    print(f"Shape 2 ({shape2_type}): Area = {area2}")
    if area1 > area2:
        print("Comparison: Shape 1 has the greater area.")
    elif area2 > area1:
        print("Comparison: Shape 2 has the greater area.")
    else:
        print("Comparison: Both shapes have equal areas.")