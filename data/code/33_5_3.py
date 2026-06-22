def compute_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    b = 10.0
    h = 5.0
    area = compute_triangle_area(b, h)
    print(area)