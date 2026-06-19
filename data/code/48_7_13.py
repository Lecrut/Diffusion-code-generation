def identify_polygon_and_semi_perimeter(sides):
    num_sides = len(sides)
    if num_sides < 3:
        return "Not a polygon", 0
    elif num_sides == 3:
        polygon_type = "Triangle"
    elif num_sides == 4:
        polygon_type = "Quadrilateral"
    else:
        polygon_type = f"{num_sides}-sided polygon"

    semi_perimeter = sum(sides) / 2
    return polygon_type, semi_perimeter

if __name__ == '__main__':
    sides_triangle = [3, 4, 5]
    sides_quadrilateral = [10, 15, 20, 25]
    sides_hexagon = [6, 6, 6, 6, 6, 6]

    polygon_type_triangle, semi_perimeter_triangle = identify_polygon_and_semi_perimeter(sides_triangle)
    print(f"Polygon Type: {polygon_type_triangle}, Semi-Perimeter: {semi_perimeter_triangle}")

    polygon_type_quadrilateral, semi_perimeter_quadrilateral = identify_polygon_and_semi_perimeter(sides_quadrilateral)
    print(f"Polygon Type: {polygon_type_quadrilateral}, Semi-Perimeter: {semi_perimeter_quadrilateral}")

    polygon_type_hexagon, semi_perimeter_hexagon = identify_polygon_and_semi_perimeter(sides_hexagon)
    print(f"Polygon Type: {polygon_type_hexagon}, Semi-Perimeter: {semi_perimeter_hexagon}")