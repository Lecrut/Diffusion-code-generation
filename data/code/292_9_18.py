def calculate_kite_perimeter(side1, side2):
    if not (isinstance(side1, (int, float)) and isinstance(side2, (int, float))):
        raise ValueError("Both sides must be numbers")
    if side1 <= 0 or side2 <= 0:
        raise ValueError("Sides must be positive")
    return 2 * (side1 + side2)

if __name__ == '__main__':
    try:
        perimeter = calculate_kite_perimeter(5, 7)
        print(perimeter)
    except ValueError as e:
        print(e)