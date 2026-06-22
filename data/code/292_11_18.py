def is_valid_triangle(side1, side2, side3):
    return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1

def calculate_perimeter(side1, side2, side3):
    if not is_valid_triangle(side1, side2, side3):
        raise ValueError("Invalid triangle sides")
    return side1 + side2 + side3

if __name__ == '__main__':
    try:
        result1 = calculate_perimeter(3, 4, 5)
        print(f"Perimeter for sides (3, 4, 5): {result1}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result2 = calculate_perimeter(7, 8, 9)
        print(f"Perimeter for sides (7, 8, 9): {result2}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        result3 = calculate_perimeter(-1, 4, 5)
    except ValueError as e:
        print(f"Error caught: {e}")