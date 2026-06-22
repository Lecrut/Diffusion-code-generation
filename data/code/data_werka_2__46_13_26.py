def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3
if __name__ == '__main__':
    side_a = 9
    side_b = 12
    side_c = 15
    perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
    print(perimeter)