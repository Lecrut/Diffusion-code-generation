def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def get_triangle_type(a, b, c):
    if not is_valid_triangle(a, b, c):
        return "invalid"
    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"

if __name__ == '__main__':
    sides_a, sides_b, sides_c = 3, 4, 5
    result_validity = is_valid_triangle(sides_a, sides_b, sides_c)
    result_type = get_triangle_type(sides_a, sides_b, sides_c)
    print(f"{result_validity}, {result_type}")
    
    sides_x, sides_y, sides_z = 1, 1, 3
    result_validity_x = is_valid_triangle(sides_x, sides_y, sides_z)
    result_type_x = get_triangle_type(sides_x, sides_y, sides_z)
    print(f"{result_validity_x}, {result_type_x}")
    
    sides_p, sides_q, sides_r = 5, 5, 5
    result_validity_p = is_valid_triangle(sides_p, sides_q, sides_r)
    result_type_p = get_triangle_type(sides_p, sides_q, sides_r)
    print(f"{result_validity_p}, {result_type_p}")