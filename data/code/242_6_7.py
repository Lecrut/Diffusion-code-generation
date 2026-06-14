import math
def calculate_regular_polygon_area(side_lengths):
    if not side_lengths:
        return 0.0
    n = len(side_lengths)
    if n < 3:
        return 0.0
    average_side = sum(side_lengths) / n
    if average_side <= 0:
        return 0.0
    area = (n * average_side**2) / (4 * math.tan(math.pi / n))
    return area
def compare_polygon_areas(sides1, sides2):
    area1 = calculate_regular_polygon_area(sides1)
    area2 = calculate_regular_polygon_area(sides2)
    if area1 > area2:
        return f"Area 1 ({area1:.4f}) is greater than Area 2 ({area2:.4f})"
    elif area1 < area2:
        return f"Area 1 ({area1:.4f}) is less than Area 2 ({area2:.4f})"
    else:
        return f"Areas are equal: {area1:.4f}"
if __name__ == '__main__':
    sides_a = [5.0, 5.0, 5.0]
    sides_b = [6.0, 6.0, 6.0]
    sides_c = [4.0, 4.0, 4.0]
    print(compare_polygon_areas(sides_a, sides_b))
    print(compare_polygon_areas(sides_a, sides_c))
    print(compare_polygon_areas(sides_b, sides_c))