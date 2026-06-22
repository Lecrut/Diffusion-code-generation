def calculate_triangle_area(base, height):
    return (base * height) / 2

if __name__ == '__main__':
    base = 10.5
    height = 7.2
    area = calculate_triangle_area(base, height)
    print(area)