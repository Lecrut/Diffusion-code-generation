def compute_surface_area(length, width, height):
    area_front = length * height
    area_side = width * height
    area_base = length * width
    total_area = 2 * (area_front + area_side + area_base)
    return total_area

if __name__ == '__main__':
    l = 5.0
    w = 3.0
    h = 2.0
    result = compute_surface_area(l, w, h)
    print(result)