def compute_triangle_area(base, height):
    half = 0.5
    product = base * height
    area = half * product
    return area

if __name__ == '__main__':
    b = 7.5
    h = 3.0
    result = compute_triangle_area(b, h)
    print(result)