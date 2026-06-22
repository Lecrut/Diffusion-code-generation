def validate_sides(sides):
    if not isinstance(sides, list) or len(sides) < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    for side in sides:
        if not isinstance(side, (int, float)) or side <= 0:
            raise ValueError("All sides must be positive numbers.")

def determine_polygon_type(num_sides):
    polygon_types = {
        3: "Triangle",
        4: "Quadrilateral"
    }
    return polygon_types.get(num_sides, f"{num_sides}-sided polygon")

def calculate_semi_perimeter(sides):
    return sum(sides) / 2

def determine_polygon_type_and_semi_perimeter(sides):
    validate_sides(sides)
    num_sides = len(sides)
    semi_perimeter = calculate_semi_perimeter(sides)
    polygon_type = determine_polygon_type(num_sides)
    return polygon_type, semi_perimeter

if __name__ == '__main__':
    sides_triangle = [3, 4, 5]
    sides_quadrilateral = [2, 2, 3, 3]
    sides_pentagon = [1, 2, 3, 4, 5]
    
    polygon_type, semi_perimeter_triangle = determine_polygon_type_and_semi_perimeter(sides_triangle)
    print(f"Polygon type: {polygon_type}, Semi-perimeter: {semi_perimeter_triangle}")
    
    polygon_type, semi_perimeter_quadrilateral = determine_polygon_type_and_semi_perimeter(sides_quadrilateral)
    print(f"Polygon type: {polygon_type}, Semi-perimeter: {semi_perimeter_quadrilateral}")
    
    polygon_type, semi_perimeter_pentagon = determine_polygon_type_and_semi_perimeter(sides_pentagon)
    print(f"Polygon type: {polygon_type}, Semi-perimeter: {semi_perimeter_pentagon}")