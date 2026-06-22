def calculate_triangle_perimeter(side1, side2, side3):
    return sum([side1, side2, side3])

if __name__ == '__main__':
    SAMPLE_SIDE_1 = 7.0
    SAMPLE_SIDE_2 = 8.5
    SAMPLE_SIDE_3 = 9.2
    perimeter = calculate_triangle_perimeter(SAMPLE_SIDE_1, SAMPLE_SIDE_2, SAMPLE_SIDE_3)
    print(perimeter)