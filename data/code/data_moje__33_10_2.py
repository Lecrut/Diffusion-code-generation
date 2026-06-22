def calculate_triangle_area(base, height):
    product = float(base) * float(height)
    area = product / 2.0
    return area

if __name__ == '__main__':
    b = 7.0
    h = 4.0
    computed_area = calculate_triangle_area(b, h)
    print(computed_area)