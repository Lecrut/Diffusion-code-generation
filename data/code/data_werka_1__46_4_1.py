def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

if __name__ == '__main__':
    side1 = 3
    side2 = 4
    side3 = 5
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)