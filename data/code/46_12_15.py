def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3
if __name__ == '__main__':
    SIDE_A = 7.5
    SIDE_B = 9.0
    SIDE_C = 12.0
    perimeter = calculate_triangle_perimeter(SIDE_A, SIDE_B, SIDE_C)
    print(perimeter)