def compute_area(rect_width, rect_height, tri_base, tri_height):
    rectangle_area = rect_width * rect_height
    triangle_area = 0.5 * tri_base * tri_height
    total_area = rectangle_area + triangle_area
    return total_area

if __name__ == '__main__':
    sample_rect_width = 10
    sample_rect_height = 6
    sample_tri_base = 8
    sample_tri_height = 5
    result = compute_area(sample_rect_width, sample_rect_height, sample_tri_base, sample_tri_height)
    print(result)