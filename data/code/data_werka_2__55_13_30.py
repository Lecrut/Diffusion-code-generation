def calculate_triangle_perimeter(a, b, c):
    REQUIRED_SIDES = 3
    MINIMUM_SIDE_LENGTH = 0

    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        raise ValueError("All sides must be numeric types.")
    if any(side <= MINIMUM_SIDE_LENGTH for side in [a, b, c]):
        raise ValueError("All sides must be positive numbers.")
    
    return sum([a, b, c])

if __name__ == '__main__':
    try:
        side1 = 6
        side2 = 8
        side3 = 10
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(perimeter)
    except ValueError as e:
        print(e)