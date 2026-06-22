def compute_triangle_area(base, height):
    return base * height / 2

if __name__ == '__main__':
    base = 10
    height = 5
    area = compute_triangle_area(base, height)
    print(area)