def determine_polygon_type_and_semi_perimeter(sides):
    if len(sides) < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    
    num_sides = len(sides)
    semi_perimeter = sum(sides) / 2
    
    polygon_names = {
        3: "Triangle",
        4: "Quadrilateral"
    }
    
    polygon_type = polygon_names.get(num_sides, f"{num_sides}-sided polygon")
    
    return polygon_type, semi_perimeter

if __name__ == '__main__':
    sides_triangle = [3, 4, 5]
    sides_quadrilateral = [2, 2, 3, 3]
    sides_hexagon = [6, 6, 6, 6, 6, 6]
    
    polygon_type_triangle, semi_perimeter_triangle = determine_polygon_type_and_semi_perimeter(sides_triangle)
    print(f"Polygon type: {polygon_type_triangle}, Semi-perimeter: {semi_perimeter_triangle}")
    
    polygon_type_quadrilateral, semi_perimeter_quadrilateral = determine_polygon_type_and_semi_perimeter(sides_quadrilateral)
    print(f"Polygon type: {polygon_type_quadrilateral}, Semi-perimeter: {semi_perimeter_quadrilateral}")
    
    polygon_type_hexagon, semi_perimeter_hexagon = determine_polygon_type_and_semi_perimeter(sides_hexagon)
    print(f"Polygon type: {polygon_type_hexagon}, Semi-perimeter: {semi_perimeter_hexagon}")