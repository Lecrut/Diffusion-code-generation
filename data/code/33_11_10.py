def compute_triangle_area(base, height):
    return 0.5 * base * height
if __name__ == '__main__':
    hardcoded_base = 10.0
    hardcoded_height = 5.0
    area = compute_triangle_area(hardcoded_base, hardcoded_height)
    print(area)