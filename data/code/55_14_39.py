def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

if __name__ == '__main__':
    SAMPLE_SIDE1 = 7
    SAMPLE_SIDE2 = 10
    SAMPLE_SIDE3 = 5
    perimeter = calculate_triangle_perimeter(SAMPLE_SIDE1, SAMPLE_SIDE2, SAMPLE_SIDE3)
    print(perimeter)