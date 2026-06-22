def is_valid_polygon(sides):
    return len(sides) > 0 and all((isinstance(side, (int, float)) and side > 0 for side in sides))

def calculate_perimeter(polygon_sides):
    if not is_valid_polygon(polygon_sides):
        return 0
    return sum(polygon_sides)
if __name__ == '__main__':
    polygon1 = [3, 4, 5]
    polygon2 = [7, 8, 9, 10]
    polygon3 = []
    print(calculate_perimeter(polygon1))
    print(calculate_perimeter(polygon2))
    print(calculate_perimeter(polygon3))