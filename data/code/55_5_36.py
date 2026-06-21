TRIANGLE_SIDES = 3

def calculate_perimeter(*sides):
    if len(sides) != TRIANGLE_SIDES:
        raise ValueError("Exactly three sides are required for a triangle.")
    return sum(sides)

if __name__ == '__main__':
    side1 = 6
    side2 = 8
    side3 = 10
    perimeter = calculate_perimeter(side1, side2, side3)
    print(perimeter)