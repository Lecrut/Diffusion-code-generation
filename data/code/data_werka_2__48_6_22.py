def determine_polygon_type_and_semi_perimeter(sides):
    if len(sides) < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    
    num_sides = len(sides)
    total_length = sum(sides)
    semi_perimeter = total_length / 2
    
    polygon_types = {
        3: "Triangle",
        4: "Quadrilateral"
    }
    
    polygon_type = polygon_types.get(num_sides, f"{num_sides}-sided polygon")
    
    return polygon_type, semi_perimeter

if __name__ == '__main__':
    sides_hexagon = [6, 6, 6, 6, 6, 6]
    sides_octagon = [8, 8, 8, 8, 8, 8, 8, 8]
    
    polygon_type_hexagon, semi_perimeter_hexagon = determine_polygon_type_and_semi_perimeter(sides_hexagon)
    print(f"Polygon type: {polygon_type_hexagon}, Semi-perimeter: {semi_perimeter_hexagon}")
    
    polygon_type_octagon, semi_perimeter_octagon = determine_polygon_type_and_semi_perimeter(sides_octagon)
    print(f"Polygon type: {polygon_type_octagon}, Semi-perimeter: {semi_perimeter_octagon}")