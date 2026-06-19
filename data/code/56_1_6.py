def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError('Length and width must be positive numbers.')
    return length * width

def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError('Base and height must be positive numbers.')
    return 0.5 * base * height

def compare_areas(rect_length, rect_width, tri_base, tri_height):
    try:
        rect_area = calculate_rectangle_area(rect_length, rect_width)
        tri_area = calculate_triangle_area(tri_base, tri_height)
        if rect_area > tri_area:
            return (rect_area, 'rectangle')
        elif tri_area > rect_area:
            return (tri_area, 'triangle')
        else:
            return (rect_area, 'rectangle')
    except ValueError as e:
        return (str(e), None)
if __name__ == '__main__':
    rect_l = 7
    rect_w = 3
    tri_b = 5
    tri_h = 6
    larger_area, shape = compare_areas(rect_l, rect_w, tri_b, tri_h)
    print(f'Larger area: {larger_area}')
    print(f'Corresponding shape: {shape}')