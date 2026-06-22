def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2, x3, y3]):
        raise ValueError("All coordinates must be numbers.")
    
    def shoelace_formula(x1, y1, x2, y2, x3, y3):
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
    
    return shoelace_formula(x1, y1, x2, y2, x3, y3)

if __name__ == '__main__':
    try:
        area = calculate_triangle_area(0, 0, 4, 0, 2, 3)
        print(area)
    except ValueError as e:
        print(e)