def triangle_interior_angle_sum():
    return 180

def quadrilateral_interior_angle_sum():
    return 360

def larger_polygon_angle_sum(triangle_sum, quadrilateral_sum):
    if triangle_sum > quadrilateral_sum:
        return "Triangle"
    else:
        return "Quadrilateral"

if __name__ == '__main__':
    triangle_sum = triangle_interior_angle_sum()
    quadrilateral_sum = quadrilateral_interior_angle_sum()
    result = larger_polygon_angle_sum(triangle_sum, quadrilateral_sum)
    print(result)