def calculate_interior_angle_sum(sides):
    return (sides - 2) * 180

def compare_polygons(triangle_sides, quadrilateral_sides):
    triangle_sum = calculate_interior_angle_sum(triangle_sides)
    quadrilateral_sum = calculate_interior_angle_sum(quadrilateral_sides)
    
    if triangle_sum > quadrilateral_sum:
        return "Triangle has a larger total interior angle sum."
    elif triangle_sum < quadrilateral_sum:
        return "Quadrilateral has a larger total interior angle sum."
    else:
        return "Both polygons have the same total interior angle sum."

if __name__ == '__main__':
    triangle_sides = 3
    quadrilateral_sides = 4
    
    result = compare_polygons(triangle_sides, quadrilateral_sides)
    print(result)