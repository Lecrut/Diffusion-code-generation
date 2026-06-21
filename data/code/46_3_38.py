def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3
if __name__ == '__main__':
    first_side = 7
    second_side = 9
    third_side = 12
    triangle_perimeter = calculate_triangle_perimeter(first_side, second_side, third_side)
    print(triangle_perimeter)