TRIANGLE_SIDES = 3

def calculate_triangle_perimeter(side1, side2, side3):
    return sum([side1, side2, side3])

if __name__ == '__main__':
    sample_sides = [7, 9, 5]
    perimeter = calculate_triangle_perimeter(*sample_sides)
    print(perimeter)