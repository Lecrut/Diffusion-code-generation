def compare_areas(rect_length, rect_width, tri_base, tri_height):
    rectangle_area = rect_length * rect_width
    triangle_area = 0.5 * tri_base * tri_height
    
    if rectangle_area > triangle_area:
        larger_area = rectangle_area
        shape = "rectangle"
    else:
        larger_area = triangle_area
        shape = "triangle"
    
    return larger_area, shape

if __name__ == '__main__':
    rect_length = 7
    rect_width = 3
    tri_base = 10
    tri_height = 6
    
    larger_area, corresponding_shape = compare_areas(rect_length, rect_width, tri_base, tri_height)
    print(f"Larger area: {larger_area}")
    print(f"Corresponding shape: {corresponding_shape}")