def compute_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    base = 10.0
    height = 5.0
    area = compute_triangle_area(base, height)
    print(area)