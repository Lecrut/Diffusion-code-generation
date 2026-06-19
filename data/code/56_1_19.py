def compare_areas(rect_length, rect_width, tri_base, tri_height):
    def area_rectangle(length, width):
        return length * width

    def area_triangle(base, height):
        return 0.5 * base * height

    rect_area = area_rectangle(rect_length, rect_width)
    tri_area = area_triangle(tri_base, tri_height)

    if rect_area > tri_area:
        return rect_area, "rectangle"
    else:
        return tri_area, "triangle"

if __name__ == '__main__':
    rect_l = 12
    rect_w = 6
    tri_b = 9
    tri_h = 5
    larger_area, shape = compare_areas(rect_l, rect_w, tri_b, tri_h)
    print(f"Larger area: {larger_area}")
    print(f"Shape: {shape}")