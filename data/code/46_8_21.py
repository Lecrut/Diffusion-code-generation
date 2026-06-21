def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

if __name__ == '__main__':
    sample_side1 = 3
    sample_side2 = 4
    sample_side3 = 5
    perimeter = calculate_triangle_perimeter(sample_side1, sample_side2, sample_side3)
    print(perimeter)