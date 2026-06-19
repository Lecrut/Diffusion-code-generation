def calculate_triangle_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

if __name__ == '__main__':
    vertices = {
        'A': (0, 0),
        'B': (4, 0),
        'C': (2, 3)
    }
    area = calculate_triangle_area(vertices['A'], vertices['B'], vertices['C'])
    print(f"Area of the triangle: {area:.2f}")