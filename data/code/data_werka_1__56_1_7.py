def compare_areas(rectangle_length, rectangle_width, triangle_base, triangle_height):
    rectangle_area = rectangle_length * rectangle_width
    triangle_area = 0.5 * triangle_base * triangle_height
    
    if rectangle_area > triangle_area:
        return rectangle_area, "rectangle"
    else:
        return triangle_area, "triangle"

if __name__ == '__main__':
    length = 10
    width = 5
    base = 8
    height = 6
    
    larger_area, shape = compare_areas(length, width, base, height)
    print(f"The larger area is {larger_area} of the {shape}.")