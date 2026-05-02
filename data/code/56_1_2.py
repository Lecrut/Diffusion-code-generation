import math
def compare_areas(rect_length, rect_width, tri_base, tri_height):
    area_rect = rect_length * rect_width
    area_tri = 0.5 * tri_base * tri_height
    if area_rect > area_tri:
        return area_rect, "rectangle"
    elif area_tri > area_rect:
        return area_tri, "triangle"
    else:
        return area_rect, "rectangle"
if __name__ == '__main__':
    rect_l = 10
    rect_w = 5
    tri_b = 10
    tri_h = 4
    larger_area, shape = compare_areas(rect_l, rect_w, tri_b, tri_h)
    print(f"Larger area: {larger_area}")
    print(f"Corresponding shape: {shape}")