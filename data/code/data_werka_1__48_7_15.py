def determine_polygon_type_and_semi_perimeter(sides):
    num_sides = len(sides)
    if num_sides < 3:
        return "Not a polygon", None
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
    sides_quadrilateral = [10, 20, 30, 40]
    sides_pentagon = [5, 5, 5, 5, 5]

    polygon_type_triangle, semi_perimeter_triangle = determine_polygon_type_and_semi_perimeter(sides_triangle)
    polygon_type_quadrilateral, semi_perimeter_quadrilateral = determine_polygon_type_and_semi_perimeter(sides_quadrilateral)
    polygon_type_pentagon, semi_perimeter_pentagon = determine_polygon_type_and_semi_perimeter(sides_pentagon)

    print(f"Polygon Type: {polygon_type_triangle}, Semi-Perimeter: {semi_perimeter_triangle}")
    print(f"Polygon Type: {polygon_type_quadrilateral}, Semi-Perimeter: {semi_perimeter_quadrilateral}")
    print(f"Polygon Type: {polygon_type_pentagon}, Semi-Perimeter: {semi_perimeter_pentagon}")