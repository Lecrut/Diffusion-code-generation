import math
def compare_areas(rect_length, rect_width, tri_base, tri_height):
    rect_area = rect_length * rect_width
    tri_area = 0.5 * tri_base * tri_height
    if rect_area > tri_area:
        return rect_area, "rectangle"
    elif tri_area > rect_area:
        return tri_area, "triangle"
    else:
        return rect_area, "rectangle"
if __name__ == '__main__':
    rect_l = 10
    rect_w = 5
    tri_b = 8
    tri_h = 4
    larger_area, shape = compare_areas(rect_l, rect_w, tri_b, tri_h)
    print(f"Larger area: {larger_area}")
    print(f"Shape: {shape}")