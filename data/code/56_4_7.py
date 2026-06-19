def calculate_interior_angle_sum(sides):
    return (sides - 2) * 180

def larger_polygon_angle_sum(triangle_sides, quadrilateral_sides):
    triangle_sum = calculate_interior_angle_sum(triangle_sides)
    quadrilateral_sum = calculate_interior_angle_sum(quadrilateral_sides)
    
    if triangle_sum > quadrilateral_sum:
        return "Triangle"
    elif quadrilateral_sum > triangle_sum:
        return "Quadrilateral"
    else:
        return "Both have equal angle sums"

if __name__ == '__main__':
    triangle_sides = 3
    quadrilateral_sides = 4
    
    result = larger_polygon_angle_sum(triangle_sides, quadrilateral_sides)
    print(result)