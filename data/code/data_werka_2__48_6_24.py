def determine_polygon_type_and_semi_perimeter(sides):
    num_sides = len(sides)
    if num_sides < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    
    polygon_types = {
        3: "Triangle",
        4: "Quadrilateral",
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon",
        9: "Nonagon",
        10: "Decagon"
    }
    
    polygon_type = polygon_types.get(num_sides, f"{num_sides}-sided polygon")
    semi_perimeter = sum(sides) / 2
    
    return polygon_type, semi_perimeter

if __name__ == '__main__':
    sides = [3, 4, 5]
    polygon_type, semi_perimeter = determine_polygon_type_and_semi_perimeter(sides)
    print(f"Polygon Type: {polygon_type}, Semi-Perimeter: {semi_perimeter}")