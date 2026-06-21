def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

if __name__ == '__main__':
    side1 = 5
    side2 = 7
    side3 = 9
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)