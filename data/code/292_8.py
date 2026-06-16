def calculate_square_perimeter(side):
    return 4 * side
def calculate_right_triangle_perimeter(a, b, c):
    return a + b + c
if __name__ == '__main__':
    square_side = 5
    square_perimeter = calculate_square_perimeter(square_side)
    print(f"Perimeter of square with side {square_side}: {square_perimeter}")
    triangle_a = 3
    triangle_b = 4
    triangle_c = 5
    triangle_perimeter = calculate_right_triangle_perimeter(triangle_a, triangle_b, triangle_c)
    print(f"Perimeter of right triangle with sides {triangle_a}, {triangle_b}, {triangle_c}: {triangle_perimeter}")