def determine_polygon_type_and_semi_perimeter(sides):
    num_sides = len(sides)
    if num_sides < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    
    semi_perimeter = sum(sides) / 2
    
    if num_sides == 3:
        return "Triangle", semi_perimeter
    elif num_sides == 4:
        return "Quadrilateral", semi_perimeter
    else:
        return f"{num_sides}-sided polygon", semi_perimeter

if __name__ == '__main__':
    sides_triangle = [3, 4, 5]
    sides_quadrilateral = [2, 2, 3, 3]
    sides_pentagon = [1, 2, 3, 4, 5]
    
    print(determine_polygon_type_and_semi_perimeter(sides_triangle))
    print(determine_polygon_type_and_semi_perimeter(sides_quadrilateral))
    print(determine_polygon_type_and_semi_perimeter(sides_pentagon))