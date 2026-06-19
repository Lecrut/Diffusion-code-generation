def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def compare_areas(rect_length, rect_width, tri_base, tri_height):
    rect_area = calculate_rectangle_area(rect_length, rect_width)
    tri_area = calculate_triangle_area(tri_base, tri_height)
    
    if rect_area > tri_area:
        return rect_area, "rectangle"
    else:
        return tri_area, "triangle"

if __name__ == '__main__':
    rectangle_length = 12
    rectangle_width = 6
    triangle_base = 9
    triangle_height = 7
    
    larger_area, shape = compare_areas(rectangle_length, rectangle_width, triangle_base, triangle_height)
    print(f"Larger area: {larger_area}")
    print(f"Corresponding shape: {shape}")