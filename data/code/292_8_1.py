def calculate_square_perimeter(side):
    return 4 * side
def calculate_right_triangle_perimeter(a, b, c):
    return a + b + c
if __name__ == '__main__':
    square_side = 5
    square_perimeter = calculate_square_perimeter(square_side)
    print(f"Perimeter of square with side {square_side}: {square_perimeter}")
    triangle_side_a = 3
    triangle_side_b = 4
    triangle_side_c = 5
    triangle_perimeter = calculate_right_triangle_perimeter(triangle_side_a, triangle_side_b, triangle_side_c)
    print(f"Perimeter of right triangle with sides {triangle_side_a}, {triangle_side_b}, {triangle_side_c}: {triangle_perimeter}")