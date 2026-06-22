def compare_areas(rectangle_length, rectangle_width, triangle_base, triangle_height):
    rectangle_area = rectangle_length * rectangle_width
    triangle_area = 0.5 * triangle_base * triangle_height
    
    if rectangle_area > triangle_area:
        return rectangle_area, "rectangle"
    else:
        return triangle_area, "triangle"

if __name__ == '__main__':
    result = compare_areas(4, 5, 3, 6)
    print(result)