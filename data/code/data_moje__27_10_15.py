def validate_non_degenerate_triangle(sides: tuple) -> bool:
    EPSILON = 1e-9
    MIN_LENGTH = 0.0
    
    if len(sides) != 3:
        return False
        
    x, y, z = sides
    
    if x <= MIN_LENGTH or y <= MIN_LENGTH or z <= MIN_LENGTH:
        return False
        
    sorted_sides = sorted([x, y, z])
    smallest_two_sum = sorted_sides[0] + sorted_sides[1]
    largest_side = sorted_sides[2]
    
    return (smallest_two_sum > largest_side) and (smallest_two_sum - largest_side > EPSILON)

if __name__ == '__main__':
    case1 = (3.0, 4.0, 5.0)
    print(validate_non_degenerate_triangle(case1))
    
    case2 = (1.0, 1.0, 2.0)
    print(validate_non_degenerate_triangle(case2))
    
    case3 = (0.1, 0.2, 0.3)
    print(validate_non_degenerate_triangle(case3))
    
    case4 = (10.0, 10.0, 10.0)
    print(validate_non_degenerate_triangle(case4))